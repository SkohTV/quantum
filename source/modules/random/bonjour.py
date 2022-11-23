'''
IMPORTS
'''

import discord
from discord import app_commands
from discord.ext import commands

import os 
from sty import fg, ef, rs # Colors https://sty.mewo.dev

from source.printC import F
from source.ids import ids

if '/' in os.path.dirname(os.path.realpath(__file__)):
	module_name = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]
	command_name = os.path.realpath(__file__).split("/")[-1].split(".")[0]
else:
	module_name = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
	command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]


'''
CLASS
'''

class Bonjour(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))


	### CUSTOMIZATION START HERE


	@app_commands.command(name="bonjour",\
	description="Souhaitez la bienvenue à Quantum, le bot du serveur !")
	@app_commands.describe(user="Utilisateur à qui souhaiter bonjour", channel="Pas de bêtises svp 😉")
	async def bonjour(self, interaction: discord.Interaction, user: discord.Member = None, channel: discord.TextChannel = None):
		if interaction.channel_id in ids.bot_channels:
			if (user == None):
				user = interaction.user
			if (channel == None):
				await interaction.response.send_message("Bonjour <@{}>".format(user.id))
			else:
				await channel.send("Bonjour <@{}>".format(user.id))
				await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel.id))


'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Bonjour(bot), guilds=[discord.Object(id=ids.guild_main)])