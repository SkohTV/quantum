"""Sync the command tree to the main guild"""
# BASE
import os

# PIP
from sty import ef, fg, rs
import discord
from discord.ext import commands

# INTERNAL
from src.utils import cprint
from src.constants import Ids



class Sync(commands.Cog):
	"""Cog class"""

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message AND DO ACTION when cog is successfully loaded"""
		# Syncing of commands
		item = await self.bot.fetch_guild(Ids.guild_main) # Get guild item
		fmt = await self.bot.tree.sync(guild=item) # Sync all commands to tree
		# Print to console
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		cprint(f"{fg(0, 135, 36)}Method loaded{fg.rs + ef.bold} -> {rs.bold_dim + command_name}")
		cprint(f"Synced {len(fmt)} commands to the current guild")
		cprint(" ")
		cprint("="*60)
		cprint(" ")
		cprint(f"{ef.bold + fg(212,175,55)}Monitoring...{fg.rs + rs.bold_dim}")
		cprint(" ")



# Smol cog class, as the module is imported as a cog for easier async call
async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(Sync(bot), guilds=[discord.Object(id=Ids.guild_main)])
