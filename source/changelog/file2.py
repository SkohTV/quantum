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
	footer_text = "Made by @Skoh#9999"

	timestamp = datetime.now()


	
	### CHANGE ###
	
	version = "v1.2.0-stable"

	update_name = "Mise en place"

	
	field['Nouveautés'] = '''
 - Création d'outils d'automatisation majeures pour le futur
 - Correction du bug d'auto déconnexion
 - Réorganisation des noms de modules
 ''' + '\u200e'

	field['Module - Random'] = '''
 - Update de la commande `/bonjour ⚪️`
 - Ajout de la commande `/cyanure ⚪️`
 '''

	field['Dev'] = '''
 - Gestion et logs des erreurs
 - Database primitive mise en place
 - Réorganisation mineure des cogs
 ''' + '\u200e'

	### CHANGE ###


	
	embed.title = f'{update_name} - {version}'
	embed.description = '\u200e'
	embed.colour = colour
	embed.set_author(name=author_name, url=github_link, icon_url=pfp_bot)
	embed.set_footer(text=footer_text, icon_url=pfp_creator)
	embed.timestamp = timestamp
	for i in field:
		embed.add_field(name=i, value=field[i], inline=False)

	return embed