import discord
from source.ids import ids
from source.printC import F


async def unmute(bot, userid):
    guild = await bot.fetch_guild(ids.guild_main)
    role = guild.get_role(ids.role_mute)
    user = await guild.fetch_member(userid)
    await user.remove_roles(role)


async def verify(bot, userid):
    guild = await bot.fetch_guild(ids.guild_main)
    role = guild.get_role(ids.role_global)
    user = await guild.fetch_member(userid)
    await user.add_roles(role)

