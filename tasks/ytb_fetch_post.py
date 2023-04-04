## Resources
#YoutubeLogoCircle = https://i.ibb.co/nfDKst5/You-Tube-social-red-circle-2017-svg.png
#YtbPlaylist = 
#Delay = 120

## Templates
#tplate_YTvideo = Hey @everyone, **Skoh** a publié une nouvelle vidéo !\n\n**I>**  https://www.youtube.com/watch?v={url}
#tplate_YTstream = Hey @here, **Skoh** est en live !!\n\n**I>**  <https://twitch.tv/SkohTV>\n**I>**  https://youtu.be/{url}
#tplate_YTshort = Hey, **Skoh** a posté un nouveau short !\n\n**I>**  https://www.youtube.com/shorts/{url}

"""Blabla"""
# BASE
import os
from datetime import datetime
import requests
import json

# PIP
from sty import ef, fg, rs
import discord
from discord.ext import commands, tasks

# INTERNAL
from database.redis_interface import Youtube as redis
from src.tools import logger
from src.constants import Ids



class YTBfetch(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.ytbfetch.start()

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		logger(fg(0, 135, 36) + 'Task started' + fg.rs + ef.bold + ' -> ' + rs.bold_dim + command_name)



	@tasks.loop(seconds=1.0, count=1)
	async def ytbfetch(self):
		# Ids
		api_key = os.environ.get("YTB_API_KEY") # Key for Youtube API
		playlist_id = "UUZEnrtgLG2qb3k7eWjuhacw" # Playlist to read from
		# Params
		parts = "snippet%2CcontentDetails"
		max_results = 10

		response = await YTB_fetch_playlist(api_key, playlist_id, parts, max_results) # Fetch videos
		response_filtered = [await redis.is_already_db(i["video_ID"]) for i in response] # Check which is already db
		
		videos = []
		types = []

		# Filter out bad
		for i in range(len(response)):
			if not response_filtered[i]:
				videos.append(response[i])
				types.append(await YTB_check_type(api_key, response[i]))

		redis.add_database(videos, types, False)



async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(YTBfetch(bot), guilds=[discord.Object(id=Ids.guild_main)])





async def YTB_fetch_playlist(api_key, playlist_id, parts, max_results):
	res = requests.get(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part={parts}&maxResults={max_results}&playlistId={playlist_id}&key={api_key}")
	data = await YTB_video_formatting(json.loads(res.text))
	return data


async def YTB_fetch_video(api_key, video_id, parts):
	res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part={parts}")
	data = json.loads(res.text)
	return data["items"][0]["snippet"]


async def YTB_check_type(api_key, video):
	data = await YTB_fetch_video(api_key, video["video_ID"], "snippet%2CcontentDetails")
	vid_type = None
	match data["liveBroadcastContent"]:
		case "live":
			vid_type = "live"
		case "upcoming":
			vid_type = "upcoming"
		case "none":
			vid_type = "short" if ("#short" in data["title"]) else "video"
	return vid_type


async def YTB_video_formatting(data):
	formated_data = []
	for i in data["items"]:
		formated_data.append({
			"channel_ID" : i["snippet"]["channelId"],
			"video_ID" : i["contentDetails"]["videoId"],
			"playlist_ID" : i["snippet"]["playlistId"],

			"channel_title" : i["snippet"]["channelTitle"],
			"title" : i["snippet"]["title"],
			"desc" : i["snippet"]["description"],
			"thumbnails" : i["snippet"]["thumbnails"],
			"format" : None
		})
	return formated_data