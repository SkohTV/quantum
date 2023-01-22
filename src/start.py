"""
Main file of the tree
This is where the bot and its components are initialized 

Order of execution : 
- main()
    - initiate token
    - start loading cog
    - bot launched
- on_ready()
    - send logs to console
    - set status
    - finish loading cog
    - threading start : post_start()
- post_start()
    - final prints
"""
import discord
from discord.ext import commands
from sty import ef, fg, rs
import asyncio
import threading
import os
import time

import src.startmsg
from src.data import Login, Setup
from src.logger import logger


src.startmsg.start() # Print starting message


"""
ON BOT START
"""
# BEFORE START
intents = discord.Intents.all() # Enable intents on https://discord.com/developers/applications
bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents) # Basic pre-requisite for the bot

@bot.event
async def on_ready():
    """Send logs to logger when bot successfully start
    - username
    - userID
    - discord.py version
    ~ all servers logged in
    ~ all cogs loaded
    """
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
    threading.Thread(target=post_start).start() # Start end of code post_start


"""
ENDING
"""
async def main():
    #async with bot: # I have no clue what this is

    for filename in os.listdir('commands'): # Iterate through file of commands
        if not (filename=="__pycache__" or os.path.isdir('commands/'+filename)):
            await bot.load_extension(f"commands.{filename[:-3]}") # Load cogs commands

    for filename in os.listdir('tasks'): # Iterate through file of tasks
        if not (filename=="__pycache__" or os.path.isdir('tasks/'+filename)):
            await bot.load_extension(f"tasks.{filename[:-3]}") # Load cogs tasks

    await bot.load_extension(f"src.sync") # Sync all commands to the guild

    print(' ')
    await bot.start(Login.TOKEN) # Start the bot with the token


def post_start():
    time.sleep(2)
    print(' ')
    logger(ef.bold + fg(212,175,55) + 'Monitoring...' + fg.rs + rs.bold_dim)
    time.sleep(3)


asyncio.run(main()) # Run main function to start the file