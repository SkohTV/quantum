"""
Methods to fetch data in CSV local files
- actionF : Fleeting actions (don't repeat)
- actionR : Repeating actions (repeat)
- permanent : Permanent actions (doesn't change)
- shift : Shifting actions (change sometimes)
"""

import csv
import os

import sys
sys.path.append('C:/Users/Utilisateur/Documents/Github/Quantum-bot')
import data

from google_auth_oauthlib.flow import InstalledAppFlow
import googleapiclient.discovery
import googleapiclient.errors



def openShift():
    # Open CSV file
    with open('db/shift.csv', 'r') as file:
        lines = list(csv.reader(file))

    # Split first column
    for i in lines:
        i[0] = i[0].split('-')

    # Do action depending on first keyword
    for i in lines:
        if i[0][0] == 'Last':
            if i[0][1] == 'YTB':
                aShiftLastYTB(i)







def aShiftLastYTB():
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    credentials="../../../../../Identifiants/credentials.json"

    flow = InstalledAppFlow.from_client_secrets_file(client_secrets_file=credentials, scopes="https://www.googleapis.com/auth/youtube.readonly")
    credentials = flow.run_console()
    youtube = googleapiclient.discovery.build(api_service_name, api_version, credentials=credentials)

    request = youtube.channels().list(part="contentDetails,snippet",forUsername="Skoh")
    response = request.execute()

    print(response)



aShiftLastYTB()