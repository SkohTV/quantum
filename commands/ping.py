"""Blabla"""
# BASE
import os
from datetime import datetime

# PIP
from sty import ef, fg, rs
import discord
from discord import app_commands
from discord.ext import commands

# INTERNAL
from src.tools import verify, logger
from src.constants import Ids



class Ping(commands.Cog):
	"""Cog class"""
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		logger(fg(0, 135, 36) + 'Command loaded' + fg.rs + ef.bold + ' -> ' + rs.bold_dim + command_name)



	# Command decorator
	@app_commands.command(name="ping", description="Renvoi le délai de Quantum entre les messages et réponses")

	# Command definition
	async def ping(self, interaction: discord.Interaction):
		"""/ping"""

		is_allowed = verify(guild=interaction.guild, channel=interaction.channel, user=interaction.user, command=os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0])
		if not is_allowed[0]: # Check if command is allowed
			await interaction.response.send_message(is_allowed[1], ephemeral=True)
			return

		# Core command code
		websocket_latency = self.bot.ws.latency
		bot_latency = self.bot.latency
		await interaction.response.send_message(content=f"Discord Bot ⇒ `{bot_latency}ms`\nDiscord Websocket ⇒ `{websocket_latency}ms`")



async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(Ping(bot), guilds=[discord.Object(id=Ids.guild_main)])
