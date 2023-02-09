"""Blablabla"""
from src.startmsg import clean_console, startmsg
from src.tests import pylint_check
from src.start import start


#clean_console() # Clear the console
#startmsg() # Print starting message

#pylint_check() # Check the code quality of the project with PyLint


#start()
#start(noverif=True)


# Command line setup todo later :
# quantum -[C][S] -[noverif] -[pylint] -[nostart]

# TESTING ZONE
from databases.cloud_access import Atlas
from modules.autopost import youtube_api as yt
from src.data import Ids, Login, Socials


#client = Atlas("Posts", "Skoh_Youtube_Short")
#client = Atlas("Posts", "Skoh_Youtube_Video")
client = Atlas("Posts", "Skoh_Youtube_Direct")

#re = yt.ytb_request_playlist("short", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty=True)
#re = yt.ytb_request_playlist("video", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty=True)
re = yt.ytb_request_playlist("direct", client, yt.ytb_connect(Login.YTB_API_KEY), "UUgmPnx-EEeOrZSg5Tiw7ZRQ", create_empty=True)




# CANNOT FETCH START / END DATE OF A DIRECT STREAM
