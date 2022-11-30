"""
Imports
"""
from src.logger import logger
from getpass import getpass
from sty import ef, fg, rs


"""
Main informations
"""
def setup_after():
    global login, version
    login = 'dev'
    version = '1.2.0'
    """A.B.C
    A = Very big additions (Birth, Odyssey)
    B = Multiple new additions
    C = Added new working addition
    delta = 'stable' for public or 'dev' for private
    """


"""
Discord ids for easy access and/or addition
"""
# ROLES
role_admin = 373070011507408896
role_modo = 452184740238327808
role_partenaire = 919308144348381264

role_xp = 406559409431642132
role_donate = 723609867625168961
role_cluster = 920074335237062718

role_global = 919287553495019530
role_mute = 463418347246321664


# CHANNELS
guild_main = 373056630004383744

channel_video = 420970924678840321
channel_dev = 975449902584840202
channel_changelog = 1034911855933669376
bot_channels = [975450909729505390, 919305979085074482]


"""
Functions to setup login informations
"""
def setup_token():
    """Grab bot token from file or stdin

    Returns:
        bool: True if token valid, else return False
    """
    # Check if TOKEN.txt exist, if not ask for manual bot token
    # TOKEN.txt is not only on my personnal computer, this script is for convenience when restarts
    global TOKEN
    setup_after()
    try:
        with open('../../Identifiants/TOKEN.TXT', 'r') as file:
            TOKEN = [line.rstrip() for line in file][0]
    except FileNotFoundError:
        logger(fg(255,0,0) + ef.bold + 'No TOKEN.txt file found' + fg.rs + rs.bold_dim + ', please provide the id here : ')
        TOKEN = getpass('')
    logger("Connecting to Discord API...")