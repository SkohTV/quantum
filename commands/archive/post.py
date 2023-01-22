"""`/post {preset} {ytb_url}`

Args
    preset
        Type of content between Stream / Vidéo / Clip
    ytb_url
        Youtube url of the content
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
class Post(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
        logger(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))


    # Command decorator
    @app_commands.command(name="post", description="Post une annonce de stream/vidéo dans le salon aquédat")
    @app_commands.describe(preset="Type d'annonce à faire", url="Url du contenu Youtube")
    @app_commands.choices(preset=[
        discord.app_commands.Choice(name="Vidéo", value="Vidéo"),
        discord.app_commands.Choice(name="Stream", value="Stream"),
        discord.app_commands.Choice(name="Clip", value="Clip"),
    ])
    @app_commands.checks.has_any_role(Ids.role_admin)

    # Command definition
    async def post(self, interaction: discord.Interaction, preset: discord.app_commands.Choice[str], url: str):

        # Core command code
        channel_video = await self.bot.fetch_channel(Ids.channel_video)
        if (preset.value == "Vidéo"):
            to_send = "Hey @everyone, **Skoh** a publié une nouvelle vidéo !\n:arrow_right: {}".format(url)
        elif (preset.value == "Stream"):
            to_send = "Hey @here, **Skoh** est en live !!\n\n\n**-->** <https://twitch.tv/SkohTV>\n**-->** {}".format(url)
        elif (preset.value == "Clip"):
            to_send = "Hey, **Skoh** à posté un nouveau clip\n:arrow_right: {}".format(url)        
        await channel_video.send(to_send)
        await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel_video.id))


"""
Cog class
"""
async def setup(bot):
    await bot.add_cog(Post(bot), guilds=[discord.Object(id=Ids.guild_main)])
