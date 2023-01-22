import googleapiclient.discovery
from src.data import Login
import json




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
    
    if create_empty:
        z = {response["items"][0]["snippet"]["channelTitle"] : []}
    else:
        z = json.load(open("video_info.json", "r+"))
    print(z)

    for item in response["items"]:
        if not item["snippet"]["channelTitle"] in z:
            z.update({
                item["snippet"]["channelTitle"] : []
                })
        if not any(d["id"] == item["snippet"]["resourceId"]["videoId"] for d in z[item["snippet"]["channelTitle"]]):
            video_info = youtube.videos().list(part='snippet,contentDetails',id=item['snippet']['resourceId']['videoId']).execute()
            print(item["snippet"]["title"])
            z[item["snippet"]["channelTitle"]].insert(0,{
                "title": item["snippet"]["title"],
                "kind": "short" if ("#short" in item["snippet"]["title"]) else ("upcoming" if video_info['items'][0]["snippet"]["liveBroadcastContent"] == "upcoming" else "video"),
                "posted": "False" if create_empty else "True",
                "id" : item["snippet"]["resourceId"]["videoId"],
                "liveBroadcastContent": video_info['items'][0]["snippet"]["liveBroadcastContent"]
                })
            print(z[item["snippet"]["channelTitle"]][-1])
            # if not create_empty:
            #     z["Skoh"].pop()
    print(z)
    json.dump(z, open("video_info.json", "w+"))





# ytb_request_playlist(ytb_connect(Login.YTB_API_KEY), "UUZEnrtgLG2qb3k7eWjuhacw", create_empty = True)
ytb_request_playlist(ytb_connect(Login.YTB_API_KEY), "UUZEnrtgLG2qb3k7eWjuhacw")