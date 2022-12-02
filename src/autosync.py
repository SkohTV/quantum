"""
After all cogs are loaded
Sync the command tree to the main guild
"""
# MUST HAVE
import os
import data
from sty import ef, fg, rs
from src.logger import logger

import discord
from discord import app_commands
from discord.ext import commands

# OTHER


"""
Cog class
""" 

class Autosync(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        try:
            # Syncing of commands
            item = await self.bot.fetch_guild(data.guild_main) # Get guild item
            fmt = await self.bot.tree.sync(guild=item) # Sync all commands to tree
            # Print to console
            command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
            logger(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))
            logger(f"Synced {len(fmt)} commands to the current guild.")
            return
        except Exception as E:
            print(E)
            
    @app_commands.command(name="aaa")
    async def sync(self, ctx):
        pass


# Smol cog class, as the module is imported as a cog for easier async call
async def setup(bot):
    await bot.add_cog(Autosync(bot), guilds=[discord.Object(id=data.guild_main)])