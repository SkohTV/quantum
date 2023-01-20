"""
Imports
"""
from src.logger import logger
from dotenv import load_dotenv
import os


"""
Load .env file
"""
dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
load_dotenv(dotenv_path)


"""
Main informations
"""
class Setup:
    login = 'dev'
    version = '2.0.0'
    """A.B.C
    A = Very big additions (Birth, Odyssey)
    B = Multiple new additions
    C = Added new working addition
    delta = 'stable' for public or 'dev' for private
    """


"""
Discord ids for easy access and/or addition
"""
class Ids:
    # Groups
    role_admin = int(os.environ.get("role_admin"))
    role_dev = int(os.environ.get("role_dev"))
    role_modo = int(os.environ.get("role_modo"))
    role_partenaire = int(os.environ.get("role_partenaire"))
    role_donateur = int(os.environ.get("role_donateur"))
    role_bot = int(os.environ.get("role_bot"))
    role_global = int(os.environ.get("role_global"))
    # Specific
    role_admin_S = int(os.environ.get("role_admin_S"))
    role_dev_S = int(os.environ.get("role_dev_S"))
    role_modo_S = int(os.environ.get("role_modo_S"))
    role_helper_S = int(os.environ.get("role_helper_S"))
    role_ytb_S = int(os.environ.get("role_ytb_S"))
    role_partenaire_S = int(os.environ.get("role_partenaire_S"))
    role_boost_S = int(os.environ.get("role_boost_S"))
    role_patreon_S = int(os.environ.get("role_patreon_S"))
    role_old_S = int(os.environ.get("role_old_S"))
    role_muted_S = int(os.environ.get("role_muted_S"))
    role_cluster_S = int(os.environ.get("role_cluster_S"))
    # Unique
    role_338223786916577281_U = int(os.environ.get("role_338223786916577281_U"))
    role_351397964700188674_U = int(os.environ.get("role_351397964700188674_U"))
    role_432683071393759242_U = int(os.environ.get("role_432683071393759242_U"))
    role_706976352150225088_U = int(os.environ.get("role_706976352150225088_U"))

    # Guilds
    guild_main = int(os.environ.get("guild_main"))
    # Unlisted
    channel_log = int(os.environ.get("channel_log"))
    channel_bot_private = int(os.environ.get("channel_bot_private"))
    channel_dev = int(os.environ.get("channel_dev"))
    # Infos
    channel_rules = int(os.environ.get("channel_rules"))
    channel_ytb = int(os.environ.get("channel_ytb"))
    channel_partner = int(os.environ.get("channel_partner"))
    channel_news = int(os.environ.get("channel_news"))
    channel_changelog = int(os.environ.get("channel_changelog"))
    # General
    channel_general = int(os.environ.get("channel_general"))
    channel_general_vip = int(os.environ.get("channel_general_vip"))
    channel_animes = int(os.environ.get("channel_animes"))
    channel_memes = int(os.environ.get("channel_memes"))
    channel_bot_public = int(os.environ.get("channel_bot_public"))
    #Private
    channel_contact_staff = int(os.environ.get("channel_contact_staff"))
    channel_private_staff = int(os.environ.get("channel_private_staff"))
    channel_private_partner = int(os.environ.get("channel_private_partner"))



"""
Exported informations (links, names, pfp, permanent texts...)
"""
class Emb: # For changelog.py
    bot_name = "Quantum"
    colour = 11900928
    author_name = "Quantum"
    pfp_bot = "https://cdn.discordapp.com/avatars/1033842126334742659/5235b0f44210455555f1685cac3580b9.png?size=1024"
    pfp_creator = "https://cdn.discordapp.com/avatars/373055398464323584/cf5191bff3d90119c78fc7156d1e32ef.png?size=1024"
    github_link = "https://github.com/SkohTV/Quantum-bot"    
    footer_text = "Made by @Skoh#9999"


"""
Functions to setup login informations
"""
class Login:
    TOKEN = os.environ.get("TOKEN")
    YTB_API_KEY = os.environ.get("YTB_API_KEY")
    MONGO_URL = os.environ.get("MONGO_URL")

"""
Not necessary anymore since I use .env files
"""
    # def setup_token():
    #     # Check if TOKEN.txt exist, if not ask for manual bot token
    #     # TOKEN.txt is not only on my personnal computer, this script is for convenience when restarts
    #     global TOKEN
    #     Setup.setup_after()
    #     try:
    #         with open('../../Identifiants/TOKEN.txt', 'r') as file:
    #             TOKEN = [line.rstrip() for line in file][0]
    #     except FileNotFoundError:
    #         logger(fg(255,0,0) + ef.bold + 'No TOKEN.txt file found' + fg.rs + rs.bold_dim + ', please provide the token here : ')
    #         TOKEN = getpass('')
    #     logger("Connecting to Discord API...")

    # def setup_api_key():
    #     # Check if API_KEY.txt exist, if not ask for manual google api key
    #     # API_KEY.txt is not only on my personnal computer, this script is for convenience when restarts
    #     global API_KEY
    #     Setup.setup_after()
    #     try:
    #         with open('../../Identifiants/API_KEY.txt', 'r') as file:
    #             API_KEY = [line.rstrip() for line in file][0]
    #     except FileNotFoundError:
    #         logger(fg(255,0,0) + ef.bold + 'No API_KEY.txt file found' + fg.rs + rs.bold_dim + ', please provide the api key here : ')
    #         API_KEY = getpass('')
    #     logger("Connecting to Google API...")