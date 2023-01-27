"""Blablabla"""
#from src.startmsg import clean_console, startmsg
#from src.tests import pylint_check
#from src.start import start


#clean_console() # Clear the console
#startmsg() # Print starting message

#pylint_check() # Check the code quality of the project with PyLint


#start()
#start(noverif=True)


# TESTING ZONE
from src.data import Login, Socials
from databases.cloud_access import Atlas
import modules.autopost.youtube_api as yt

temp = Atlas("Posts", "Skoh_Youtube")
yt.ytb_request_playlist(temp, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty=True)
temp.disconnect()
