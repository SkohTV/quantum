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
	module_name = "MAIN"
	command_name = os.path.realpath(__file__).split("/")[-1].split(".")[0]
else:
	module_name = "MAIN"
	command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]


'''
CLASS
'''

class Autosync(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))


	@commands.command()
	async def sync(self,ctx) -> None:
		fmt = await ctx.bot.tree.sync(guild=ctx.guild)
		await ctx.send(
			f"Synced {len(fmt)} commands to the current guild."
		)
		return


'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Autosync(bot), guilds=[discord.Object(id=ids.guild_main)])