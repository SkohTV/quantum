"""
Main file of the tree
This is where the bot and its components are initialized

Order of execution :
- bot_init()
		- create bot object
- main()
		- initiate token
		- start loading cog
		- bot launched
- on_ready()
		- send logs to console
		- set status
		- finish loading cog
"""
# BASE
import os
import asyncio

# PIP
import discord
from discord.ext import commands
from sty import ef, fg, rs

# INTERNAL
from src.data import Login, Setup
from src.tools import logger



def start():
	"""bot_init()"""
	intents = discord.Intents.all() # Enable intents on https://discord.com/developers/applications
	bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents) # Basic pre-requisite for the bot


	async def main():
		"""main()"""
		# Load commands
		for filename in os.listdir('commands'): # Iterate through file of commands
			if not (filename=="__pycache__" or os.path.isdir('commands/'+filename)):
				await bot.load_extension(f"commands.{filename[:-3]}") # Load cogs commands

		await bot.load_extension("src._sync") # Sync all commands to the guild
		print(' ')
		await bot.start(Login.TOKEN) # Start the bot with the token


	@bot.event
	async def on_ready():
		"""on_ready()"""
		# Print bot infos
		print(' ')
		logger('Logged with username ' + fg(0,255,0) + bot.user.name + fg.rs)
		logger('Logged with userID ' + fg(0,255,255) + str(bot.user.id) + fg.rs)
		logger('Discord module version is ' + fg(0,255,255) + str(discord.__version__) + fg.rs)
		# Print guilds connected to (should only be one)
		print(' ')
		logger(fg(255,0,0) + ef.underl + 'Servers connected to:' + rs.underl + fg.rs)
		for guild in bot.guilds:
			logger('- ' + guild.name)

		print(' ')
		logger(ef.bold + fg(212,175,55) + 'Cogs loading...' + fg.rs + rs.bold_dim)
		# Change status of the bot
		bot_version = f'v{Setup.version}-{Setup.login}' # Get version from src.data file
		await bot.change_presence(activity=discord.Game(name=bot_version))



	asyncio.run(main()) # Run main function to start the file
