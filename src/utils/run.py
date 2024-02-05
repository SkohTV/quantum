import discord
from dotenv import load_dotenv

import os
from discord.ext import commands

import asyncio



def run():
  # Create the bot object and load .env
  intents = discord.Intents.all() # Enable intents on https://discord.com/developers/applications
  bot = commands.Bot(command_prefix="q!", case_insensitive=True, intents=intents) # Create bot object (requiered)
  bot_version = "3.0.0-rework"

  # .env
  dotenv_path = os.path.join(os.getcwd(), ".env")
  load_dotenv(dotenv_path)

  @bot.event
  async def on_ready():
    """on_ready()"""
    # Print bot infos
    print()
    print(f"Logged with username {bot.user.name}")
    print(f"Logged with userID {bot.user.id}")
    print(f"Discord module version is {discord.__version__}")
    # Print guilds connected to (should only be one)
    print('\nServers connected to:')
    for guild in bot.guilds:
      print(f"- {guild.name}")
    print()
    print('\nCogs loading...')
    # Change status of the bot
    # bot_version = f"v{Setup.version}-{Setup.login}" # Get version from src.data file
    await bot.change_presence(activity=discord.Game(name=bot_version))


  async def load_modules(bot):
    await bot.load_extension('src.commands.ping') # Ping command

    await bot.load_extension('src.utils.sync') # Sync all commands to guilds


  async def start_bot(bot):
    await bot.start(os.environ.get('DISCORD_BOT_TOKEN'))


  # Load commands / events / tasks, then sync
  asyncio.run(load_modules(bot))
  
  # Start the bot
  asyncio.run(start_bot(bot))

