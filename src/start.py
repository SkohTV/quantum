"""Blabla"""
# BASE
import os
import asyncio

# PIP
import discord
from discord.ext import commands
from sty import ef, fg, rs
from dotenv import load_dotenv

# INTERNAL
from src.constants import Setup
from src.utils import cprint



def start():
	"""bot_init()"""
	intents = discord.Intents.all() # Enable intents on https://discord.com/developers/applications
	bot = commands.Bot(command_prefix="q!", case_insensitive=True, intents=intents) # Create bot object (requiered)
	dotenv_path = os.path.join(os.getcwd(), ".env") # Look for the .env file
	load_dotenv(dotenv_path) # Load the .env

	async def main():
		"""main()"""
		# Load commands
		for filename in os.listdir("commands"): # Iterate through file of commands
			if not (filename=="__pycache__" or os.path.isdir("commands/"+filename)):
				await bot.load_extension(f"commands.{filename[:-3]}") # Load cogs commands

		# Load commands
		for filename in os.listdir("tasks"): # Iterate through file of tasks
			if not (filename=="__pycache__" or os.path.isdir("tasks/"+filename)):
				await bot.load_extension(f"tasks.{filename[:-3]}") # Load tasks

		await bot.load_extension("src._sync") # Sync all commands to the guild
		cprint(" ")

		await bot.start(os.environ.get("TOKEN")) # Start the bot with the token


	@bot.event
	async def on_ready():
		"""on_ready()"""
		# Print bot infos
		cprint(" ")
		cprint(f"Logged with username {fg(0,255,0)}bot.user.name{fg.rs}")
		cprint(f"Logged with userID {fg(0,255,255) + str(bot.user.id) + fg.rs}")
		cprint(f"Discord module version is {fg(0,255,255) + str(discord.__version__) + fg.rs}")
		# Print guilds connected to (should only be one)
		cprint(" ")
		cprint(f"{fg(255,0,0) + ef.underl}Servers connected to:{rs.underl + fg.rs}")
		for guild in bot.guilds:
			cprint("- " + guild.name)

		cprint(" ")
		cprint(f"{ef.bold + fg(212,175,55)}Cogs loading...{fg.rs + rs.bold_dim}")
		# Change status of the bot
		bot_version = f"v{Setup.version}-{Setup.login}" # Get version from src.data file
		await bot.change_presence(activity=discord.Game(name=bot_version))



	asyncio.run(main()) # Run main function to start the file
