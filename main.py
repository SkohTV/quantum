'''
IMPORTS
'''

print(' ')
print(' ')
import pip
from source.printC import F

def import_or_install(package):
    try:
        __import__(package)
    except ImportError:
        pip.main(['install', package])


# PIP MODULES
import_or_install('asyncio')
import_or_install('flask')
import_or_install('sty') 
import_or_install('discord')


import asyncio
import os
import threading

import time
from pathlib import Path
from getpass import getpass
from sty import fg, ef, rs # Colors https://sty.mewo.dev

# https://discordpy.readthedocs.io/en/stable/api.html
import discord
from discord.ext import commands

from source import check


'''
CORE CODE
'''

# BEFORE START
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents)

# WHEN START
bot_version = "v1.2.0-new"
"""A.B.C
A = Very big additions (Birth, Odyssey)
B = Multiple new additions
C = Added new working addition
Delta = 'stable' if stable, 'dev' if Quantum Dev , 'unstable' if bug known, 'new' if new patch (for 1 week)
"""

@bot.event
async def on_ready():
	print(' ')
	print(F('Logged with username ' + fg(0,255,0) + bot.user.name + fg.rs))
	print(F('Logged with userID ' + fg(0,255,255) + str(bot.user.id) + fg.rs))
	print(F('Discord module version is ' + fg(0,255,255) + str(discord.__version__) + fg.rs))
	print(' ')
	print(F(fg(255,0,0) + ef.underl + 'Servers connected to:' + rs.underl + fg.rs))
	for guild in bot.guilds:
		print(F('- ' + guild.name))
	print(' ')
	print(F(ef.bold + fg(212,175,55) + 'Cogs loading...' + fg.rs + rs.bold_dim))
	await bot.change_presence(activity=discord.Game(name=bot_version))
	threading.Thread(target=post_start).start()


'''
LOADING COMMANDS
'''
	
# MAIN MODULE
async def load_main():
	await bot.load_extension("source.modules.autosync") #Load sync command
	await bot.load_extension("source.check") #Load autocheck code
	return

# RANDOM MODULE
async def load_random():
	await bot.load_extension("source.modules.random.bonjour")
	await bot.load_extension("source.modules.random.changelog")
	await bot.load_extension("source.modules.random.cyanure")
	return
	
# AUTOPOST MODULE
async def load_autopost():
	await bot.load_extension("source.modules.autopost.post")
	return


'''
TESTING ZONE
'''





'''
ENDING
'''

# Check if TOKEN.txt exist, if not ask for manual bot token
# TOKEN.txt is not only on my personnal computer, this script is for convenience when restarts
try:
	with open('../../Identifiants/TOKEN.TXT', 'r') as file:
		TOKEN = [line.rstrip() for line in file][0]
except FileNotFoundError:
	print(F(fg(255,0,0) + ef.bold + 'No TOKEN.txt file found' + fg.rs + rs.bold_dim + ', please provide the id here : '))
	TOKEN = getpass('')
print(F("Connecting to Discord API..."))


async def main():
	async with bot:
		await load_autopost()
		await load_random()
		await load_main()
		print(' ')
		await bot.start(TOKEN)


def post_start():
	time.sleep(1)
	print(' ')
	print(F(ef.bold + fg(212,175,55) + 'Monitoring...' + fg.rs + rs.bold_dim))
	#threading.Thread(target=check.autocheck).start()
		


asyncio.run(main())


'''
LIENS
'''

# https://www.youtube.com/watch?v=-D2CvmHTqbE