"""`/changelog {version} {channel}`

Args
	version
		version of the changelog to send
	channel
		channel to send changelog into

Action
	send_message
		Send created message to Discord guild
"""
# BASE
import os
import json
from datetime import datetime

# PIP
from sty import ef, fg, rs
import discord
from discord import app_commands
from discord.ext import commands

# INTERNAL
from src.verify import verify
from src.logger import logger
from src.data import Ids
from src.data import Emb



class Changelog(commands.Cog):
	"""Cog class"""

	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		"""Send message when cog is successfully loaded"""
		command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
		logger(fg(0, 135, 36) + 'Command loaded' + fg.rs + ef.bold + ' -> ' + rs.bold_dim + command_name)



	# Command decorator
	@app_commands.command(name="changelog", description="Envoyer le changelog d'une version dans un salon")
	@app_commands.describe(version="Version du changelog à envoyer", channel="Channel dans lequel envoyer le changelog")
	@app_commands.choices(version=[discord.app_commands.Choice(name=i, value=i) for i in json.load(open('databases/changelog.json', 'r', encoding='utf-8'))]) # Create a choice for all index in json file
	@app_commands.choices(channel=[
		discord.app_commands.Choice(name="🔐devs-bot", value="🔐devs-bot"),
		discord.app_commands.Choice(name="📚changelog", value="📚changelog")
	])
	@app_commands.checks.has_any_role(Ids.role_admin)

	# Command definition
	async def changelog(self, interaction: discord.Interaction, version: str, channel: str):
		"""/changelog {version} {channel}"""

		is_allowed = verify(guild=interaction.guild, channel=interaction.channel, user=interaction.user, command=os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0])
		if not is_allowed[0]: # Check if command is allowed
			await interaction.response.send_message(is_allowed[1], ephemeral=True)
			return

		# Core command code
		# Open changelog.json
		with open('databases/changelog.json', 'r', encoding='utf-8') as clog:
			memory = json.load(clog)
		memory = memory[version]

		# Create embed
		embed = discord.Embed()
		fields = {}

		# Imports from changelog.json
		fields = memory['fields']

		# Formatting
		embed.title = f'{memory["title"]} - {version}'
		embed.description = '\u200e'
		embed.colour = Emb.colour
		embed.url = Emb.github_link
		embed.set_author(name=Emb.author_name, icon_url=Emb.pfp_bot)
		embed.set_footer(text=Emb.footer_text, icon_url=Emb.pfp_creator)
		for i in fields:
			string = str()
			for j in fields[i]:
				string += j+"\n"
			embed.add_field(name=i, value=string, inline=False)
		timestamp = datetime.now()
		embed.timestamp = timestamp

		# Send message
		to_send = embed
		channel_obj = self.bot.get_channel(Ids.channel_dev) if channel == "🔐devs-bot" else self.bot.get_channel(Ids.channel_changelog)
		await channel_obj.send(embed=to_send)
		await interaction.response.send_message(f":white_check_mark: __Message envoyé__ **->** <#{channel_obj.id}>")




async def setup(bot):
	"""Cog setup"""
	await bot.add_cog(Changelog(bot), guilds=[discord.Object(id=Ids.guild_main)])
