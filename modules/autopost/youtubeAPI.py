import googleapiclient.discovery
from src.data import Login, Socials
from src import logger
import json
import time




def ytb_connect(API_KEY: str) -> googleapiclient.discovery.Resource:
    """Create a connection to the Youtube API

    Args:
        API_KEY (str): Given API key located in the .env file

    Returns:
        googleapiclient.discovery.Resource: Youtube object to use for requests
    """
    api_service_name, api_version, DEVELOPER_KEY = "youtube", "v3", API_KEY
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    return youtube



def ytb_request_playlist(youtube: googleapiclient.discovery.Resource, playlistId: str, maxResults = 20, create_empty = False):
    """Send a request to Youtube API to fetch videos from a playlist

    Args:
        youtube (googleapiclient.discovery.Resource): Initialized Youtube object to connect to Youtube API
        playlistId (str): The ID of the playlist to fetch
        maxResults (int, optional): Max number of results to fetch (20 almost every time)
        create_empty (bool, optional): If True, create a new json file with the channel name as key and an empty list as value. Defaults to False.
    """
    request = youtube.playlistItems().list(
        part='snippet',
        maxResults=maxResults,
        playlistId=playlistId
    )
    response = request.execute()
    
    z = [] if create_empty else json.load(open("video_info.json", "r+"))
    if not create_empty:
        z.reverse()


    for item in response["items"]:
        if not any(d["id"] == item["snippet"]["resourceId"]["videoId"] for d in z):
            video_info = youtube.videos().list(part='snippet,contentDetails',id=item['snippet']['resourceId']['videoId']).execute()
            z.append({
                "title": item["snippet"]["title"],
                "kind": "short" if ("#short" in item["snippet"]["title"]) else ("upcoming" if video_info['items'][0]["snippet"]["liveBroadcastContent"] == "upcoming" else "video"),
                "posted": "False" if create_empty else "True",
                "id" : item["snippet"]["resourceId"]["videoId"],
                "liveBroadcastContent": video_info['items'][0]["snippet"]["liveBroadcastContent"]
                })
            

    if not create_empty:
        while(len(z) > 20):
            z.pop(0)
        z.reverse()
    json.dump(z, open("video_info.json", "w+"))




def init():
    ytb_request_playlist(ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty = True)


# init()
# ytb_request_playlist(ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)