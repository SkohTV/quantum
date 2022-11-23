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

class Post(commands.Cog):
	def __init__(self, bot: commands.Bot):
		self.bot = bot

	@commands.Cog.listener()
	async def on_ready(self):
		print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))

		
	### CUSTOMIZATION START HERE

		
	@app_commands.command(name="post",\
	description="Post une annonce de stream/vidéo dans le salon aquédat")
	@app_commands.describe(preset="Type d'annonce à faire", url="Url du contenu Youtube")
	@app_commands.choices(preset=[
		discord.app_commands.Choice(name="Vidéo", value="Vidéo"),
		discord.app_commands.Choice(name="Stream", value="Stream"),
		discord.app_commands.Choice(name="Stream", value="Clip"),
	])
	@app_commands.checks.has_any_role(ids.role_admin)
	async def post(self, interaction: discord.Interaction, preset: discord.app_commands.Choice[str], url: str):
		if interaction.channel_id in ids.bot_channels:
			channel_video = await self.bot.fetch_channel(ids.channel_video)
			if (preset.value == "Vidéo"):
				to_send = "Hey @everyone, **Skoh** a publié une nouvelle vidéo !\n:arrow_right: {}".format(url)
			elif (preset.value == "Stream"):
				to_send = "Hey @everyone, **Skoh** est en live !!\n\n\n**-->** <https://twitch.tv/SkohTV>\n**-->** {}".format(url)
			elif (preset.value == "Clip"):
				to_send = "Hey, **Skoh** à posté un nouveau clip\n:arrow_right: {}".format(url)		
			await channel_video.send(to_send)
			await interaction.response.send_message(":white_check_mark: __Message envoyé__ **->** <#{}>".format(channel_video.id))


'''
COG SETUP
'''

async def setup(bot):
	await bot.add_cog(Post(bot), guilds=[discord.Object(id=ids.guild_main)])