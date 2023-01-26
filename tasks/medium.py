"""Medium loop
Loop every 1 min

Actions :
- Posts
		- Youtube update DB
		- Youtube posts
		- Other RS update DB
		- Other RS posts
"""
# MUST HAVE
import os
import asyncio
from sty import ef, fg, rs

import discord
# from discord import app_commands
from discord.ext import commands, tasks

from src.data import Ids
from src.logger import logger
from src.verify import verify




class Medium(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot
		self.medium.start()

	def start_task(self):
		self.medium.start()

	@commands.Cog.listener()
	async def on_ready(self):
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		logger(fg(0, 135, 36) + 'Task loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))



	# Command decorator
	@tasks.loop(seconds=10.0)
	async def medium(self):
		print("aaaa")



	# Wait until bot ready before starting task
	@medium.before_loop
	async def before_medium(self):
		await self.bot.wait_until_ready()
		await asyncio.sleep(5)


async def setup(bot):
	"""Add the cog to the tree"""
	await bot.add_cog(Medium(bot), guilds=[discord.Object(id=Ids.guild_main)])