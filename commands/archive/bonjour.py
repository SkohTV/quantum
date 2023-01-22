"""`/bonjour [user] [channel]`

Args
    user (optionnal)
        user to greet (default is same as interaction)
    channel (optional)
        channel to send message in (default is same as interaction)
Action
    send_message
        Send created message to Discord guild
"""
# MUST HAVE
import os
from src.data import Ids
from sty import ef, fg, rs
from src.logger import logger

import discord
from discord import app_commands
from discord.ext import commands

# OTHER


"""
Cog class
"""
class Bonjour(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
        logger(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))


    # Command decorator
    @app_commands.command(name="bonjour",\
    description="Souhaitez la bienvenue à Quantum, le bot du serveur !")
    @app_commands.describe(user="Utilisateur à qui souhaiter bonjour", channel="Pas de bêtises svp 😉")

    # Command definition
    async def bonjour(self, interaction: discord.Interaction, user: discord.Member = None, channel: discord.TextChannel = None):

        # Core command code
        if (user == None):
            user = interaction.user
        if (channel == None):
            await interaction.response.send_message("Bonjour <@{}>".format(user.id))
        else:
            await channel.send("Bonjour <@{}>".format(user.id))
            await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel.id))


"""
Cog setup
"""
async def setup(bot):
    await bot.add_cog(Bonjour(bot), guilds=[discord.Object(id=Ids.guild_main)])