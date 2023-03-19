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
	# Perms
	role_admin = 373070011507408896
	role_dev = 1046844434987368479
	role_modo = 452184740238327808
	role_partenaire = 919308144348381264
	role_cluster = 1086752176442986616
	role_donateur = 723609867625168961
	role_bot = 416290253125582848
	role_global = 919287553495019530
	# Specific
	role_U_admin = 479697709884899328
	role_U_modo = 373070046056153090
	role_U_helper = 919302463260065842
	role_U_ytb = 373070230781427712
	role_U_patreon = 1056404075945660546
	role_U_patreon_T3 = 1086751844589633647
	role_U_patreon_T2 = 1086751819943911598
	role_U_patreon_T1 = 1086751699970035712
	role_U_partenaire = 441329802763436033
	role_U_boost = 1043582235380555857
	role_U_old = 406559409431642132
	role_U_muted = 463418347246321664
	# Unique
	role_U_Sari_Osbad = 479697766101155867
	role_U_LucUp = 496389361105895435
	role_U_Illun = 791121963355078676
	role_U_Dunky = 785130358973661216

	# Guilds
	guild_main = 373056630004383744
	# Unlisted
	channel_log = 1046187380761174078
	channel_bot_private = 919305979085074482
	channel_dev = 975449902584840202
	# Infos
	channel_rules = 422489846754443266
	channel_ytb = 420970924678840321
	channel_partner = 919292968861593631
	channel_news = 393840817124540447
	channel_changelog = 1034911855933669376
	channel_welcome = 1079430152691400724
	# General
	channel_general = 919292528510001213
	channel_general_vip = 919292838146093097
	channel_animes = 1041170354032365568
	channel_memes = 1041170328572928100
	channel_bot_public = 975450909729505390
	#Private
	channel_contact_staff = 975452567771414620
	channel_private_staff = 975452610117107722
	channel_private_partner = 975452641347919892
	# VC
	VC_channel_public_1 = 977693061192753152
	VC_channel_public_2 = 977712600756404295
	VC_waiting = 977699261263265862
	VC_private = 978051082355896330


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
