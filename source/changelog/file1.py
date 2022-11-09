'''
IMPORTS
'''

import discord
from datetime import datetime


'''
FUNCTION
'''

def convert():
	embed=discord.Embed()
	field = dict()
	
	#PERMANENT
	bot_name = "Quantum"
	colour = 11900928
	
	author_name = "Quantum"
	pfp_bot = "https://cdn.discordapp.com/avatars/1033842126334742659/5235b0f44210455555f1685cac3580b9.png?size=1024"
	
	pfp_creator = "https://cdn.discordapp.com/avatars/373055398464323584/cf5191bff3d90119c78fc7156d1e32ef.png?size=1024"
	github_link = "https://github.com/SkohTV/Quantum"
	timestamp = datetime.now()


	
	### CHANGE ###
	
	version = "v1.0.0-alpha"

	update_name = "Naissance"

	
	field['Nouveautés'] = '''
 - Apparition soudaine de <@1033842126334742659>
 - Écriture du README.md
 ''' + '\u200e'

	field['Module - Random'] = '''
 - Création du module
 - Ajout de la commande `/bonjour ⚪️`
 - Ajout de la commande `/changelog 🔴`
 '''

	field['Module - Autopost'] = '''
 - Création du module
 - Ajout de la commande `/post 🔴`
 ''' + '\u200e'

	### CHANGE ###


	
	embed.title = f'{update_name} - {version}'
	embed.description = '\u200e'
	embed.colour = colour
	embed.set_author(name=author_name, icon_url=pfp_bot)
	embed.set_footer(text=github_link, icon_url=pfp_creator)
	embed.timestamp = timestamp
	for i in field:
		embed.add_field(name=i, value=field[i], inline=False)

	return embed