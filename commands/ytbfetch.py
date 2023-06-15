"""Blabla"""
# BASE
import os
import json
import requests

# PIP
from sty import ef, fg, rs
import discord
from discord import app_commands
from discord.ext import commands

# INTERNAL
from src.utils import verify, cprint
from src.constants import Ids



class Ytbfetch(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.videos = []
		self.monitor = []

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		cprint(f"{fg(0, 135, 36)}Command loaded{fg.rs + ef.bold} -> {rs.bold_dim + command_name}")



	# Command decorator
	@app_commands.command(name="ytbfetch", description="Fetch les vidéos de la chaine de Skoh")

	# Command definition
	async def ping(self, interaction: discord.Interaction):
		"""/ytbfetch"""

		is_allowed = verify(guild=interaction.guild, channel=interaction.channel, user=interaction.user, command=os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0])
		if not is_allowed[0]: # Check if command is allowed
			await interaction.response.send_message(is_allowed[1], ephemeral=True)
			return

		# Core command code
		response_msg = "Fetching videos for **Skoh**..."
		await interaction.response.send_message(content=response_msg)
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
					response_msg += f"\nSuccessfully sent **video** __{i['title']}__"
					await interaction.edit_original_response(content=response_msg)
				elif i["format"] == "short":
					webhook.send(f"Hey, **{i['channel_title']}** a posté un nouveau short !\n\n**▷**  https://www.youtube.com/shorts/{i['video_ID']}")
					response_msg += f"\nSuccessfully sent **short** __{i['title']}__"
					await interaction.edit_original_response(content=response_msg)
				elif i["format"] == "live":
					webhook.send(f"Hey @here, **{i['channel_title']}** est en live !!\n\n**▷**  https://youtu.be/{i['video_ID']}")
					response_msg += f"\nSuccessfully sent **stream** __{i['title']}__"
					await interaction.edit_original_response(content=response_msg)
		else:
			response_msg += "\nNo new videos found"


		response_msg += "\nSuccessfully fetched videos"
		try:
			await interaction.edit_original_response(content=response_msg)
		except Exception as e:
			cprint(e.__repr__(), status="error")



async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(Ytbfetch(bot), guilds=[discord.Object(id=Ids.guild_main)])




############################################
#								CORE COMMANDS							 #
############################################


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
