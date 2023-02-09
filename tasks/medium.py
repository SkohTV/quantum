"""Medium loop
Loop every 1 min

Actions :
- Posts
		- Youtube update DB
		- Youtube posts
		- Other RS update DB
		- Other RS posts
"""
# BASE
import os
import asyncio

# PIP
from sty import ef, fg, rs
import discord
from discord.ext import commands, tasks

# INTERNAL
from src.logger import logger
from src.data import Ids, Login, Socials
from databases.cloud_access import Atlas
from modules.autopost import youtube_api as yt

# PYLINT
# False Positive : Method 'medium' has no 'start' memberPylint(E1101:no-member)
# (Must stay in comments)
# pylint: disable=no-member



class Medium(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		logger(fg(0, 135, 36) + 'Task loaded' + fg.rs + ef.bold + ' -> ' + rs.bold_dim + command_name)
		self.medium.start()



	# Task decorator
	@tasks.loop(seconds=60.0)

	# Task definition
	async def medium(self):
		"""Main loop starts here"""
		logger(ef.bold + fg(120, 191, 242) + 'Medium loop ' + fg(0, 135, 36) + 'is starting' + fg.rs + rs.bold_dim)

		client = Atlas("Posts", "Skoh_Youtube")

		new_vids = yt.ytb_request_playlist("video", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)
		for video in new_vids:
			await post_skoh_ytb(self.bot, video)

		await schedule_skoh_ytb(self.bot)

		client.disconnect()







	@medium.before_loop
	async def before_medium(self):
		"""Wait until bot ready before starting task"""
		await self.bot.wait_until_ready()
		await asyncio.sleep(5)


async def setup(bot):
	"""Add the cog to the tree"""
	await bot.add_cog(Medium(bot), guilds=[discord.Object(id=Ids.guild_main)])




# ACTIONS

async def post_skoh_ytb(bot: commands.Bot, video_data: dict) -> None:
	"""Post a video or short to Discord channel

	Args:
		bot (commands.Bot): Bot object to post/fetch
		video_data (dict): Raw data of the fetched new video
	"""
	match video_data["kind"]:
		case "video":
			channel_video = await bot.fetch_channel(Ids.channel_dev)
			url = f"https://youtube.com/watch?v={video_data['id']}"
			await channel_video.send(f"Hey @everyone, **Skoh** a publié une nouvelle vidéo !\n:arrow_right: {url}")
		case "short":
			channel_video = await bot.fetch_channel(Ids.channel_dev)
			url = f"https://www.youtube.com/shorts/{video_data['id']}"
			await channel_video.send(f"Hey, **Skoh** à posté un nouveau clip\n:arrow_right: {url}")



async def schedule_skoh_ytb(bot: commands.Bot) -> None:
	"""Create a scheduled event from a Youtube Livestream (auto update each loop)

	Args:
		bot (commands.Bot): Bot object to post/fetch
	"""
	main_guild = await bot.fetch_guild(Ids.guild_main)
	events = await main_guild.fetch_scheduled_events()

	# Fetch livestream DB

	livestreams = []

	for stream in livestreams:
		for event in events:
			if not stream == event.location:
				# TO CREATE :  location (will be kept forever), subject, desc, image, start date, start time, end date, end time
				# CREATE EVENT
				pass
			else:
				# TO CHECK :  subject, desc, image, start date, start time, end date, end time
				# IF check param by param
					# update
				pass

	# Check if exist
	# If not, create
	# If exist, check differences
	# If differences, update

	# Find a solution to delete event if live finished
	# Need to separate db for video / shorts / livestreams



"""
Hey @here, **Skoh** est en live !!

**-->** https://twitch.tv/SkohTV
**-->** https://youtube.com/live/{url}
"""
