'''
IMPORTS
'''


import discord
from discord import app_commands
from discord.ext import commands

import os 

from source.ids import ids

module_name = os.path.dirname(os.path.realpath(__file__)).split("\\")[-1]
command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]
		
	
'''
CLASS
'''

class Post(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print('Cog loaded -> {} / {}'.format(module_name,command_name))

		
	### CUSTOMIZATION START HERE

		
	@app_commands.command(name="post",\
	description="Post une annonce de stream/vidéo dans le salon aquédat")
	@app_commands.describe(preset="Type d'annonce à faire", url="Url du contenu Youtube")
	@app_commands.choices(preset=[
		discord.app_commands.Choice(name="Youtube", value=1),
		discord.app_commands.Choice(name="Twitch", value=2),
	])
	@app_commands.checks.has_any_role(ids.role_admin)
	async def post(self, interaction: discord.Interaction, preset: discord.app_commands.Choice[int], url: str):
		if interaction.channel_id in ids.bot_channels:
			channel_video = await self.bot.fetch_channel(ids.channel_video)
			if (preset.value == 1):
				to_send = "Hey @everyone, **Skoh** a publié une nouvelle vidéo\n:arrow_right: {}".format(url)
			elif (preset.value == 2):
				to_send = "Hey @everyone, **SkohTV** est en live !!\n\n\n**-->** <https://twitch.tv/SkohTV>\n**-->** {}".format(url)		
			await channel_video.send(to_send)
			await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel_video.id))


'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Post(bot), guilds=[discord.Object(id=ids.guild_main)])