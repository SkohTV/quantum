



import discord
from data import Ids




def verify(guild: discord.Guild, user: discord.Member = None, channel: discord.TextChannel = None, command: str = None) -> bool:
    """Check if command is allowed to be used in this guild, channel and by this user

    Args:
        guild (discord.Guild): Guild in which the message was sent
        user (discord.Member): User that sent the message
        channel (discord.TextChannel): Channel where the message was sent
        command (str): Command that was executed

    Returns:
        (bool, string): If command is allowed, and if not why
    """
    if not guild.id == Ids.guild_main:
        return (False, "❌ Commande désactivée dans ce serveur")

    # Changelog command -> Check IF channel in bot_channels AND user has admin role
    if command == "changelog":
        if (channel.id in Ids.bot_channels):
            if (Ids.role_admin in list(map(lambda x: x.id, user.roles))):
                return (True, None)
            else:
                return (False, "❌ Vous n'avez pas la permission d'utiliser cette commande")
        else:
            return (False, "❌ Commande désactivée dans ce salon")

    # Ping command -> Check IF channel in bot_channels
    if command == "ping":
        if (channel.id in Ids.bot_channels):
            return (True, None)
        else:
            return (False, "❌ Commande désactivée dans ce salon")

    return (False, "❌ Aucune commande n'a été spécifiée dans le code")