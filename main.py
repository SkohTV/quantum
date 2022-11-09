'''
IMPORTS

PIP :
- flask
- sty
- discord
'''
print('\n\n\n')


#from source.keep_alive import keep_alive # Keep the script running
#import os # For keep_alive
import asyncio # To start async main

from sty import fg, ef, rs # Colors https://sty.mewo.dev


# https://discordpy.readthedocs.io/en/stable/api.html

import discord # All discord commands
from discord.ext import commands # For bot = commands...


'''
CORE CODE
'''

# PRE_START

intents = discord.Intents.all()
bot = commands.Bot(command_prefix='q!', case_insensitive=True, intents=intents)


# ON_START

@bot.event
async def on_ready():
	print('')
	print('Logged with username ' + fg(0,255,0) + bot.user.name + fg.rs)
	print('Logged with userID ' + fg(0,255,255) + str(bot.user.id) + fg.rs)
	print('Discord module version is ' + fg(0,255,255) + str(discord.__version__) + fg.rs)
	print('')
	print(fg(255,0,0) + ef.underl + 'Servers connected to:' + rs.underl + fg.rs)
	for guild in bot.guilds:
		print('- ' + guild.name)
	print('')
	print(ef.bold + fg(212,175,55) + 'Cogs loading...' + fg.rs + rs.bold_dim)
	
	await bot.change_presence(activity=discord.Game(name="v1.0.3-alpha"))


'''
LOADING COMMANDS
'''

	
#MAIN MODULE
async def load_main():
	await bot.load_extension("source.modules.autosync") #Load sync command
	return

#RANDOM MODULE
async def load_random():
	await bot.load_extension("source.modules.random.bonjour") # Say hello in response
	await bot.load_extension("source.modules.random.changelog") # Post changelog in channel
	await bot.load_extension("source.modules.random.cyanure") # Punish the user more or less heavily
	return
	
#AUTOPOST MODULE
async def load_autopost():
	await bot.load_extension("source.modules.autopost.post") # Post notif video/stream + @everyone
	return


'''
ENDING
'''

# TEMPORARY SOLUTION TO GET TOKEN (NOT SAFE (THINK TO DELETE TOKEN.txt))
with open("TOKEN.txt") as file:
	TOKEN = [line.rstrip() for line in file][0]


async def main():
	async with bot:
		await load_autopost()
		await load_random()
		await load_main()
		await bot.start(TOKEN)


#keep_alive()
asyncio.run(main())


'''
TESTING ZONE
'''






'''
LIENS
'''

# https://www.youtube.com/watch?v=-D2CvmHTqbE