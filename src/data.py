"""Global Variables that will be shared across all scripts"""
import os
from dotenv import load_dotenv


# Load .env file
dotenv_path = os.path.join(os.getcwd(), '.env')
load_dotenv(dotenv_path)



class Setup:
	"""Main informations"""
	login = 'dev'
	version = '2.0.0'
	"""A.B.C
	A = Very big additions (Birth, Odyssey)
	B = Multiple new additions
	C = Added new working addition
	delta = 'stable' for public or 'dev' for private
	"""



class Ids:
	# Groups
	role_admin = 
	role_dev = 
	role_modo = 
	role_partenaire = 
	role_donateur = 
	role_bot = 
	role_global = 
	# Specific
	role_admin_S = 
	role_dev_S = 
	role_modo_S = 
	role_helper_S = 
	role_ytb_S = 
	role_partenaire_S = 
	role_boost_S = 
	role_patreon_S = 
	role_old_S = 
	role_muted_S = 
	role_cluster_S = 
	# Unique
	role_338223786916577281_U = 
	role_351397964700188674_U = 
	role_432683071393759242_U = 
	role_706976352150225088_U = 

	# Guilds
	guild_main = 
	# Unlisted
	channel_log = 
	channel_bot_private = 
	channel_dev = 
	# Infos
	channel_rules = 
	channel_ytb = 
	channel_partner = 
	channel_news = 
	channel_changelog = 
	# General
	channel_general = 
	channel_general_vip = 
	channel_animes = 
	channel_memes = 
	channel_bot_public = 
	#Private
	channel_contact_staff = 
	channel_private_staff = 
	channel_private_partner = 


class Emb: # For changelog.py
	"""Exported informations (links, names, pfp, permanent texts...)"""
	bot_name = "Quantum"
	colour = 11900928
	author_name = "Quantum"
	pfp_bot = "https://cdn.discordapp.com/avatars/1033842126334742659/5235b0f44210455555f1685cac3580b9.png?size=1024"
	pfp_creator = "https://cdn.discordapp.com/avatars/373055398464323584/cf5191bff3d90119c78fc7156d1e32ef.png?size=1024"
	github_link = "https://github.com/SkohTV/Quantum-bot"
	footer_text = "Made by @Skoh#9999"



class Login: # For changelog.py
	"""Discord Bot Token"""
	TOKEN = int(os.environ.get("TOKEN"))
