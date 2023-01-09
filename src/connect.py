API_KEY = ""

# -*- coding: utf-8 -*-

# Sample Python code for youtube.playlistItems.list
# See instructions for running these code samples locally:
# https://developers.google.com/explorer-help/code-samples#python
import googleapiclient.discovery
import json

def ytb_connect():
    api_service_name, api_version, DEVELOPER_KEY = "youtube", "v3", API_KEY
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    return youtube

def ytb_request_playlist(youtube: googleapiclient.discovery.Resource, maxResults: int, playlistId: str):
    request = youtube.playlistItems().list(
        part="snippet",
        maxResults=maxResults,
        playlistId=playlistId
    )
    response = request.execute()
    for item in response["items"]:
        print(item["snippet"]["title"])
    return response

def ytb_request_direct(youtube: googleapiclient.discovery.Resource, maxResults: int, channelId: str):
    global API_KEY
    request = youtube.liveBroadcasts().list(
        part='id,snippet,contentDetails',
        broadcastStatus='active',
        broadcastType='all',
        key=API_KEY
    )
    response = request.execute()
    return response




youtube = ytb_connect()
ytb_request_playlist(youtube, 5, "UULFZEnrtgLG2qb3k7eWjuhacw")
ytb_request_playlist(youtube, 5, "PLFZfkJ-Hknm-S6UoD1IScocIk8rhkoLp2")
ytb_request_direct(youtube, 5, "UCLFZEnrtgLG2qb3k7eWjuhacw")
