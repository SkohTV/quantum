"""Blablabla"""
from src.startmsg import clean_console, startmsg
from src.tests import pylint_check
#from src.start import start


clean_console() # Clear the console
startmsg() # Print starting message

pylint_check() # Check the code quality of the project with PyLint


#start()
#start(noverif=True)


# TESTING ZONE

#import databases.cloudAccess
#import modules.autopost.youtubeAPI
