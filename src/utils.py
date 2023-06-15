"""Blabla"""
# BASE
import os
import platform
from datetime import datetime

# PIP
import discord
from sty import fg #, ef, rs

# INTERNAL
from src.constants import Ids



############################################
#							 		PRINT/LOG								 #
############################################

def cprint(text: str, status: str = "base", kind: str = "stdi") -> None:
	"""Receive all stdout and process them

	Args:
		text (str): Message to add to logs seen on console and discord msg logs
		specific (tuple): Custom kind of notification to log (priority, error...)
	"""
	now = str(datetime.now())
	time = f"[{now[0:4]}-{now[5:7]}-{now[8:10]} {now[11:13]}:{now[14:16]}:{now[17:19]}]"

	match status:
		case "waiting":
			time = f"{fg(212,175,55) + time + fg.rs}"
		case "error":
			time = f"{fg(255,0,0) + time + fg.rs}"
		case "success":
			time = f"{fg(0,255,0) + time + fg.rs}"

	message = f"{time} {text}"

	match kind:
		case "stdi":
			print(message)
		case "file":
			pass
		case "logs":
			pass




############################################
#						 CHECK PERMISSIONS						 #
############################################

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

	# Do something depending on the command
	match command:

# Changelog command -> Check IF channel in bot_channels AND user has admin role
		case "changelog":
			if not (channel.id in [Ids.channel_bot_private, Ids.channel_bot_public]): # Check if message is in valid channel
				return (False, "❌ Commande désactivée dans ce salon")
			if not Ids.role_admin in list(map(lambda x: x.id, user.roles)): # Check if user has role admin
				return (False, "❌ Vous n'avez pas la permission d'utiliser cette commande")
			return (True, None) # Good !


	# Ping command -> Check IF channel in bot_channels
		case "ping":
			if not (channel.id in [Ids.channel_bot_private, Ids.channel_bot_public]): # Check if message is in valid channel
				return (False, "❌ Commande désactivée dans ce salon")
			return (True, None)


	# Ping command -> Check IF channel in bot_channels
		case "ytbfetch":
			if not (channel.id in [Ids.channel_bot_private, Ids.channel_bot_public]): # Check if message is in valid channel
				return (False, "❌ Commande désactivée dans ce salon")
			return (True, None) # Good !

	# When no command is specified (dev error)
		case _:
			return (False, "❌ Aucune commande n'a été spécifiée dans le code")




############################################
#								START MESSAGE							 #
############################################

def clean_console():
	"""Clear the terminal"""
	match platform.system:
		case "Linux":
			os.system('clear')
		case "Windows":
			os.system('cls')
		case "Darwin":
			pass # I don't know the clear screen for macos
		case _:
			cprint(text="")

def startmsg():
	"""Cool starting message"""
	print("""



                                   ,,,,,,,,,,,,,,,
                            .,,,,,,,,,,*******,,,,,,,,,
                        ,,,,,,,,,,,,**,,*************,,,,,,
                     ,,,,,,,,,,,,,,**********************,,,,.
                  ,,,,,,,,,,,,,,***************************,,,,,
                ,,,,////******//******************************,,,,
              ,,,,////******//////////**************************,,,
            ,,,,//,//******/////////********/////****************,,,,
           ,,,/      ******/////////*******///////////*************,,,
          ,,,/       ******//////////*******///////////**      *///*,,,
         ,,,//.    ,*******/%//////////////////////////*        /////,,,
        ,,,//////////***%%%%%%%%%%%%%%%%%%%%%%%%//////**,       //////,,.
        ,,((((/////////%%%%%%%%%%%%%%%%%%%%%%%%%%////*********/////////,,
        **((((((((((((%%%%%%%%%%%%%%%%%%%%%%%%%%%%**********///////////,,
        **(((((((((((/,%%%%%%%%%##############%%%%*******//////////////**,
       ***(((((((((((#%%%%%%%###################%,***//////////////////**
     ***/((((((((((((%%%%%%%%################,(((///////////////////**
         //((((((((((*,****,%%%###########%(,,((((((((((((//////////**.
          //((((((((((((((((((((/*,**,,*/((((((((((((((((((((((((((/////////
                          ////((((((//.
                              ((((((
              /(((((((((((((((((((((((((((((((((((((((((((((*
             (((((((((((((((((((((((((((((((((((((((((((((((((
                                         (((((((((
                               ,(((((((((((((((((((((((/
                              (((((((((((((((((((((((((((


         █████╗  ██╗   ██╗ █████╗ ███╗   ██╗████████╗██╗   ██╗███╗   ███╗
        ██╔═══██╗██║   ██║██╔══██╗████╗  ██║╚══██╔══╝██║   ██║████╗ ████║
        ██║   ██║██║   ██║███████║██╔██╗ ██║   ██║   ██║   ██║██╔████╔██║
        ██║▄▄ ██║██║   ██║██╔══██║██║╚██╗██║   ██║   ██║   ██║██║╚██╔╝██║
        ╚██████╔╝╚██████╔╝██║  ██║██║ ╚████║   ██║   ╚██████╔╝██║ ╚═╝ ██║
         ╚══▀▀═╝  ╚═════╝ ╚═╝  ╚═╝╚═╝  ╚═══╝   ╚═╝    ╚═════╝ ╚═╝     ╚═╝

""")
