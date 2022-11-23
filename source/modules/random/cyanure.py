'''
IMPORTS
'''

import discord
from discord import app_commands
from discord.ext import commands

import os, asyncio
from sty import fg, ef, rs # Colors https://sty.mewo.dev

from source.printC import F
from source.ids import ids
from source import check

import datetime

if '/' in os.path.dirname(os.path.realpath(__file__)):
	module_name = os.path.dirname(os.path.realpath(__file__)).split("/")[-1]
	command_name = os.path.realpath(__file__).split("/")[-1].split(".")[0]
else:
	module_name = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
	command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]


'''
CLASS
'''

class Cyanure(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))

		
	### CUSTOMIZATION START HERE

		
	@app_commands.command(name="cyanure",\
	description="Un suicide assisté par un bot fantastique !")
	@app_commands.describe(force="L'intensité de la sanction")
	@app_commands.choices(force=[
		discord.app_commands.Choice(name="Faible", value=1),
		discord.app_commands.Choice(name="Moyen", value=2),
		discord.app_commands.Choice(name="Fort", value=3),
	])
	async def cyanure(self, interaction: discord.Interaction, force: discord.app_commands.Choice[int]):
		try:
			if not interaction.channel_id in ids.bot_channels:
				return
			item = await self.bot.fetch_guild(ids.guild_main)
			item = [item.get_role(ids.role_mute), item.get_role(ids.role_global)]
			if (force.value==1):
				await interaction.response.send_message("Vous avez subi une faible punition")
				await interaction.user.add_roles(item[0])
				check.add_check(f'unmute-{interaction.user.id}', (datetime.datetime.now()+datetime.timedelta(minutes=5)))
			elif (force.value==2):
				await interaction.response.send_message("Vous avez été puni sévèrement")
				await interaction.user.add_roles(item[0])
				check.add_check(f'unmute-{interaction.user.id}', (datetime.datetime.now()+datetime.timedelta(hours=1)))
			elif (force.value==3):
				await interaction.response.send_message("Vous avez de tendances suicidaires")
				await interaction.user.remove_roles(item[1])
				check.add_check(f'verify-{interaction.user.id}', (datetime.datetime.now()+datetime.timedelta(hours=10)))
		except Exception as E:
			print(F(E))
			

'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Cyanure(bot), guilds=[discord.Object(id=ids.guild_main)])