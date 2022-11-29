'''
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
'''
import discord
from discord.ext import commands
from sty import ef, fg, rs
import asyncio
import threading
import os
import time

import data
from src.printer import printer


'''
ON BOT START
'''
# BEFORE START
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents)
bot_version = f'v{data.version}-{data.login}'

@bot.event
async def on_ready():
	print(' ')
	printer('Logged with username ' + fg(0,255,0) + bot.user.name + fg.rs)
	printer('Logged with userID ' + fg(0,255,255) + str(bot.user.id) + fg.rs)
	printer('Discord module version is ' + fg(0,255,255) + str(discord.__version__) + fg.rs)
	print(' ')
	printer(fg(255,0,0) + ef.underl + 'Servers connected to:' + rs.underl + fg.rs)
	for guild in bot.guilds:
		printer('- ' + guild.name)
	print(' ')
	printer(ef.bold + fg(212,175,55) + 'Cogs loading...' + fg.rs + rs.bold_dim)
	await bot.change_presence(activity=discord.Game(name=bot_version))
	threading.Thread(target=post_start).start()


'''
ENDING
'''
async def main():
    print(' \n ')
    #print(' ')
    data.setup_token()
    async with bot:
        for filename in os.listdir('commands'): # Iterate through file of commands
            bot.load_extension(f"commands.{filename}") # Add command to cog
        print(' ')
        await bot.start(data.TOKEN)

def post_start():
	time.sleep(1)
	print(' ')
	printer(ef.bold + fg(212,175,55) + 'Monitoring...' + fg.rs + rs.bold_dim)
	#threading.Thread(target=check.autocheck).start()
		

asyncio.run(main())