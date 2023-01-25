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
# MUST HAVE
import os
from src.data import Ids
from sty import ef, fg, rs
from src.logger import logger
from src.verify import verify

import discord
from discord import app_commands
from discord.ext import commands

# OTHER
from datetime import datetime
from src.data import Emb
import json


"""
Cog class
"""
class Changelog(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot
        
    @commands.Cog.listener()
    async def on_ready(self):
        command_name = os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0]
        logger(fg(0, 135, 36) + 'Command loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {}'.format(command_name))



    # Command decorator
    @app_commands.command(name="changelog",\
    description="Envoyer le changelog d'une version dans un salon")
    @app_commands.describe(version="Version du changelog à envoyer", channel="Channel dans lequel envoyer le changelog")
    @app_commands.choices(version=[discord.app_commands.Choice(name=i, value=i) for i in json.load(open('databases/changelog.json', 'r', encoding='utf-8'))]) # Create a choice for all index in json file
    @app_commands.choices(channel=[
        discord.app_commands.Choice(name="🔐devs-bot", value="🔐devs-bot"),
        discord.app_commands.Choice(name="📚changelog", value="📚changelog")
    ])
    @app_commands.checks.has_any_role(Ids.role_admin)

    # Command definition
    async def changelog(self, interaction: discord.Interaction, version: str, channel: str):

        isAllowed = verify(guild=interaction.guild, channel=interaction.channel, user=interaction.user, command=os.path.realpath(__file__).split("/")[-1].split("\\")[-1].split(".")[0])
        if not isAllowed[0]: # Check if command is allowed
            await interaction.response.send_message(isAllowed[1], ephemeral=True)
            return

        # Core command code
        # Open changelog.json
        with open('databases/changelog.json', 'r', encoding='utf-8') as f:
            memory = json.load(f)
        memory = memory[version]

        # Create embed
        embed=discord.Embed()
        fields = dict()

        # Imports from changelog.json
        version_bot = version
        update_name = memory['title']
        fields = memory['fields']

        # Permanent informations
        bot_name = Emb.bot_name
        colour = Emb.colour
        author_name = Emb.author_name
        pfp_bot = Emb.pfp_bot
        pfp_creator = Emb.pfp_creator
        github_link = Emb.github_link   
        footer_text = Emb.footer_text

        # Formatting
        embed.title = f'{update_name} - {version_bot}'
        embed.description = '\u200e'
        embed.colour = colour
        embed.url = github_link
        embed.set_author(name=author_name, icon_url=pfp_bot)
        embed.set_footer(text=footer_text, icon_url=pfp_creator)
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
        await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel_obj.id))


"""
Cog setup
"""
async def setup(bot):
    await bot.add_cog(Changelog(bot), guilds=[discord.Object(id=Ids.guild_main)])