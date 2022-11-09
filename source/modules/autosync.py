'''
IMPORTS
'''


import discord
from discord.ext import commands

import os 
from sty import fg, ef, rs

from source.ids import ids

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
		print('Cog loaded -> {} / {}'.format(module_name,command_name))
		print('')
		print(ef.bold + fg(212,175,55) + 'Monitoring...' + fg.rs + rs.bold_dim)

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