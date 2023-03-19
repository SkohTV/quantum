"""`/ping`

Action
	send_message
		Send message -> then edit with delay between interaction and response
"""
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
from src.data import Ids



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
		first = datetime.now().timestamp()
		await interaction.response.send_message(":hourglass: Loading...")
		second = datetime.now().timestamp()
		third = interaction.created_at.timestamp()#replace(tzinfo=None)# + timedelta(hours=1)
		delay = round((second - first)*1000,2)
		delay2 = abs(round((third - first)*1000,1))
		await interaction.edit_original_response(content=f"Discord Bot ⇒ `{delay2}ms`\nDiscord Servers ⇒ `{delay}ms`")




async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(Ping(bot), guilds=[discord.Object(id=Ids.guild_main)])
