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

		
	@app_commands.command(name="cy",\
	description="Blablabla")
	@app_commands.describe(force="Blablabla")
	@app_commands.choices(force=[
		discord.app_commands.Choice(name="Faible", value=1),
		discord.app_commands.Choice(name="Moyen", value=2),
		discord.app_commands.Choice(name="Fort", value=3),
	])
	async def cyanure(self, interaction: discord.Interaction, force: discord.app_commands.Choice[int]):
		if not interaction.channel_id in ids.bot_channels:
			return
		if (force.value==1):
			await interaction.response.send_message("A")
			await asyncio.sleep(3)
			print("a")
			await interaction.edit_original_response(content="B")
		else:
			print("2")
			

'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Cyanure(bot), guilds=[discord.Object(id=ids.guild_main)])