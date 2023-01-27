"""
Main file of the tree
This is where the bot and its components are initialized

Order of execution :
- bot_init()
		- create bot object
- module_test()
		- load .env
		- load mongoDB
- main()
		- initiate token
		- start loading cog
		- bot launched
- on_ready()
		- send logs to console
		- set status
		- finish loading cog
		- final prints
"""
import os
import asyncio

import discord
from discord.ext import commands
from sty import ef, fg, rs
from dotenv import load_dotenv
from pymongo.errors import ServerSelectionTimeoutError

from src.data import Login, Setup
from src.logger import logger
from databases import cloud_access as cAccess



def start(noverif=False):
	"""bot_init()"""
	intents = discord.Intents.all() # Enable intents on https://discord.com/developers/applications
	bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents) # Basic pre-requisite for the bot



	def module_test():
		"""module_test()"""

		# Test if.env file exists
		print(' ')
		logger(ef.bold + fg(212,175,55) + '.env is loading...' + fg.rs + rs.bold_dim)
		dotenv_path = os.path.join(os.getcwd(), '.env')
		load_dotenv(dotenv_path)
		if not os.environ.get("verif") == "True":
			logger(ef.bold + '.env is ' + fg(255,0,0) + 'not valid'+ fg.rs + rs.bold_dim)
		else:
			logger(ef.bold + '.env is ' + fg(0, 135, 36) + 'valid' + fg.rs + rs.bold_dim)

    # Test if MongoDB is running
		print(' ')
		logger(ef.bold + fg(212,175,55) + 'MongoDB Client is loading...' + fg.rs + rs.bold_dim)
		try:
			client_temp = cAccess.connect()
			client_temp.list_database_names()
			cAccess.disconnect(client_temp)
			logger(ef.bold + 'MongoDB Client is ' + fg(0, 135, 36) + 'valid' + fg.rs + rs.bold_dim)
		except ServerSelectionTimeoutError as err:
			logger(ef.bold + 'MongoDB Client is ' + fg(255,0,0) + 'not valid'+ fg.rs + rs.bold_dim + ' -> ' + str(type(err)).replace("<class 'pymongo.errors.", "")[:-2])




	async def main():
		"""main()"""
		#async with bot: # I have no clue what this is

		for filename in os.listdir('commands'): # Iterate through file of commands
			if not (filename=="__pycache__" or os.path.isdir('commands/'+filename)):
				await bot.load_extension(f"commands.{filename[:-3]}") # Load cogs commands

		for filename in os.listdir('tasks'): # Iterate through file of tasks
			if not (filename=="__pycache__" or os.path.isdir('tasks/'+filename)):
				await bot.load_extension(f"tasks.{filename[:-3]}") # Load cogs tasks

		await bot.load_extension("src.sync") # Sync all commands to the guild

		print(' ')
		await bot.start(Login.TOKEN) # Start the bot with the token



	@bot.event
	async def on_ready():
		"""on_ready()"""

		print(' ')
		logger('Logged with username ' + fg(0,255,0) + bot.user.name + fg.rs)
		logger('Logged with userID ' + fg(0,255,255) + str(bot.user.id) + fg.rs)
		logger('Discord module version is ' + fg(0,255,255) + str(discord.__version__) + fg.rs)

		print(' ')
		logger(fg(255,0,0) + ef.underl + 'Servers connected to:' + rs.underl + fg.rs)
		for guild in bot.guilds:
			logger('- ' + guild.name)

		print(' ')
		logger(ef.bold + fg(212,175,55) + 'Cogs loading...' + fg.rs + rs.bold_dim)
		# Last setups with the on_ready event not logs related
		bot_version = f'v{Setup.version}-{Setup.login}' # Get version from src.data file
		await bot.change_presence(activity=discord.Game(name=bot_version)) # Initiate discord bot status message
		# threading.Thread(target=post_start).start() # Start end of code post_start



	# Launch the script
	if not noverif:
		module_test() # Show error messages if modules don't work (MongoDB, .env)
		asyncio.run(main()) # Run main function to start the file
