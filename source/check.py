import datetime, time

import discord
from discord.ext import tasks, commands
import asyncio
import os

from sty import fg, ef, rs # Colors https://sty.mewo.dev

from source.printC import F
from source import take_action
from source.ids import ids


if '/' in os.path.dirname(os.path.realpath(__file__)):
	module_name = "MAIN"
	command_name = os.path.realpath(__file__).split("/")[-1].split(".")[0]
else:
	module_name = "MAIN"
	command_name = os.path.realpath(__file__).split("\\")[-1].split(".")[0]


file_link = 'source/database/checks.txt'
form = '[TIMED_CHECK]'
time_out = 60 # Seconds


def add_check(name:str, time:datetime.datetime):
        format = f"{time.year}.{time.month}.{time.day}.{time.hour}.{time.minute}.{time.second}"
        with open(file_link, 'a') as f:
            f.write(f'{name}:{format}\n')
        print(F(f"{form} Added check : {name}"))


def remove_check(name:str):
    all_checks = list()
    with open(file_link, 'r') as file:
        for line in file:
            to_format = line.rstrip()
            to_format = to_format.split(':', 1)
            if not to_format[0] == name:
                all_checks.append(line.rstrip())
    with open(file_link, 'w') as file:
        for line in all_checks:
            file.write(line) 
    print(F(f"{form} Removed check : {name}"))


def get_checks():
    all_checks = list()
    to_format = list()
    with open(file_link) as file:
        for line in file:
            to_format = line.rstrip()
            to_format = to_format.split(':', 1)
            to_format[1] = to_format[1].split('.')
            to_format[1] = [int(i) for i in to_format[1]]
            to_format[1] = datetime.datetime(year=to_format[1][0], month=to_format[1][1], day=to_format[1][2], hour=to_format[1][3], minute=to_format[1][4], second=to_format[1][5])
            all_checks.append(to_format)
        return all_checks


def timecheck(datetime_time_theoric: datetime.datetime):
    time_remain = datetime_time_theoric - datetime.datetime.now()
    if (time_remain > datetime.timedelta()):
        return (False, time_remain)
    else:
        return (True, time_remain)


async def send_action(bot, action: str):
    try:
        print(F(f"{form} Processing action : {action}"))
        action = action.split('-')
        if action[0]=='unmute':
            await take_action.unmute(bot, action[1])
        elif action[0]=='verify':
            await take_action.verify(bot, action[1])
        elif action=='pass':
            pass
    except Exception as E:
        print(F(E))





# Cog setup
class Check(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(F(fg(0, 135, 36) + 'Cog loaded' + fg.rs + ef.bold + ' ->' + rs.bold_dim + ' {} / {}'.format(module_name,command_name)))
        time.sleep(2)
        self.autocheck.start()

    
    @tasks.loop(seconds=time_out)
    async def autocheck(self):
        try: 
            checks_backup = get_checks()
            for i in checks_backup:
                if timecheck(i[1])[0]:
                    await send_action(self.bot, i[0])
                    remove_check(i[0])
            print(F(f"{form} All checks have been verified"))
        except Exception as E:
            print(F(E))


async def setup(bot):
    await bot.add_cog(Check(bot), guilds=[discord.Object(id=ids.guild_main)])