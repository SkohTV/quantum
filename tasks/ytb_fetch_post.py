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
import json
import asyncio

# PIP
import requests
from sty import ef, fg, rs
import discord
from discord.ext import commands, tasks

# INTERNAL
from src.utils import cprint
from src.constants import Ids



class YTBfetch(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.ytbfetch.start()
		self.videos = []
		self.monitor = []

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		cprint(fg(0, 135, 36) + 'Task started' + fg.rs + ef.bold + ' -> ' + rs.bold_dim + command_name)



	@tasks.loop(seconds=120.0)
	async def ytbfetch(self):
		cprint(f"Fetching videos for {ef.bold}Skoh{rs.bold_dim}...", status="waiting")
		# Ids
		api_key = os.environ.get("YTB_API_KEY") # Key for Youtube API
		playlist_id = "UUZEnrtgLG2qb3k7eWjuhacw" # Playlist to read from
		# Params
		parts = "snippet%2CcontentDetails"
		max_results = 10

		response = await YTB_fetch_playlist(api_key, playlist_id, parts, max_results) # Fetch videos
		to_send = []
		if not response: return # Handles rate limit

		# If no videos in memory, don't send
		do_send = (not self.videos == [])

#		# Filter out bad
		for i in response:
			for j in self.videos:
				if i["video_ID"] == j["video_ID"]:
					break
			else:
				i.update({"format" : await YTB_check_type(api_key, i)})
				if i["format"] == "video" or i["format"] == "short" or i["format"] == "live":
					self.videos.append(i)
					to_send.append(i)

		while len(self.videos) > 50:
			self.videos.pop(0)


		if do_send:
			webhook = discord.SyncWebhook.from_url(os.environ.get("WebhookYTB"))
			for i in to_send:
				if i["format"] == "video":
					webhook.send(f"Hey @everyone, **{i['channel_title']}** a publié une nouvelle vidéo !\n\n**▷**  https://www.youtube.com/watch?v={i['video_ID']}")
					cprint(f"Successfully sent {ef.bold}video{rs.bold_dim} {ef.underl + i['title'] + rs.underl} for {ef.bold}Skoh{rs.bold_dim}")
				elif i["format"] == "short":
					webhook.send(f"Hey, **{i['channel_title']}** a posté un nouveau short !\n\n**▷**  https://www.youtube.com/shorts/{i['video_ID']}")
					cprint(f"Successfully sent {ef.bold}short{rs.bold_dim} {ef.underl + i['title'] + rs.underl} for {ef.bold}Skoh{rs.bold_dim}")
				elif i["format"] == "live":
					webhook.send(f"Hey @here, **{i['channel_title']}** est en live !!\n\n**▷**  https://youtu.be/{i['video_ID']}")
					cprint(f"Successfully sent {ef.bold}stream{rs.bold_dim} {ef.underl + i['title'] + rs.underl} for {ef.bold}Skoh{rs.bold_dim}")

		cprint(f"Successfully fetched videos for {ef.bold}Skoh{rs.bold_dim}", status="success")




	@ytbfetch.before_loop
	async def wait(self):
		await self.bot.wait_until_ready()
		await asyncio.sleep(5)


async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(YTBfetch(bot), guilds=[discord.Object(id=Ids.guild_main)])




async def YTB_fetch_playlist(api_key, playlist_id, parts, max_results):
	try:
		res = requests.get(f"https://youtube.googleapis.com/youtube/v3/playlistItems?part={parts}&maxResults={max_results}&playlistId={playlist_id}&key={api_key}")
		data = await YTB_video_formatting(json.loads(res.text))
		return data
	except Exception as e:
		cprint(e.__repr__(), status="error")
		return False

async def YTB_fetch_video(api_key, video_id, parts):
	try:
		res = requests.get(f"https://www.googleapis.com/youtube/v3/videos?id={video_id}&key={api_key}&part={parts}")
		data = json.loads(res.text)
		return data["items"][0]["snippet"]
	except Exception as e:
		cprint(e.__repr__(), status="error")
		return False


async def YTB_check_type(api_key, video):
	data = await YTB_fetch_video(api_key, video["video_ID"], "snippet%2CcontentDetails")
	if not data: return False # Handle rate limit
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
			"format" : None,
		})
	return formated_data