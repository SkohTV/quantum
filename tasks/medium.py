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
	@tasks.loop(seconds=10.0)

	# Task definition
	async def medium(self):
		"""Main loop starts here"""
		client = Atlas("Posts", "Skoh_Youtube")

		new_vids = yt.ytb_request_playlist(client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)

		client.disconnect()







	# Wait until bot ready before starting task
	# @medium.before_loop
	# async def before_medium(self):
	# 	await self.bot.wait_until_ready()
	# 	await asyncio.sleep(5)

async def setup(bot):
	"""Add the cog to the tree"""
	await bot.add_cog(Medium(bot), guilds=[discord.Object(id=Ids.guild_main)])
