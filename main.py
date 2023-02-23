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
re = yt.ytb_request_playlist("direct", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty=True)

#yt.ytb_create_creds(Login.YTB_ACCESS_TOKEN, Login.YTB_REFRESH_TOKEN, Login.YTB_CLIENT_ID, Login.YTB_CLIENT_SECRET)

#re = yt.ytb_request_playlist("short", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)
#re = yt.ytb_request_playlist("video", client, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)


# CANNOT FETCH START / END DATE OF A DIRECT STREAM















#from google.oauth2.credentials import Credentials
#from google_auth_oauthlib.flow import InstalledAppFlow

## Set up the OAuth 2.0 flow
#flow = InstalledAppFlow.from_client_secrets_file('client_secret.json', scopes=['https://www.googleapis.com/auth/youtube.force-ssl'])
#creds = flow.run_local_server(port=0)

## Save the credentials for later use
#creds_dict = {'access_token': creds.token, 'refresh_token': creds.refresh_token, 'token_uri': creds.token_uri, 'client_id': creds.client_id, 'client_secret': creds.client_secret, 'expires_in': creds.expiry}
#print(creds_dict)