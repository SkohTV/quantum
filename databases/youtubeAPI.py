import googleapiclient.discovery
from data import Login
import json




def ytb_connect(API_KEY: str):
    """_summary_

    Args:
        API_KEY (str): _description_

    Returns:
        _type_: _description_
    """
    api_service_name, api_version, DEVELOPER_KEY = "youtube", "v3", API_KEY
    youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = DEVELOPER_KEY)
    return youtube

def ytb_request(youtube: googleapiclient.discovery.Resource, maxResults: int, playlistId: str):
    """_summary_

    Args:
        youtube (googleapiclient.discovery.Resource): _description_
        maxResults (int): _description_
        playlistId (str): _description_
    """
    request = youtube.playlistItems().list(
        part='snippet',
        maxResults=20,
        playlistId=playlistId
    )
    response = request.execute()
    z = json.load(open("video_info.json", "r+"))

    for item in response["items"]:
        if not item["snippet"]["channelTitle"] in z:
            z.update({
                item["snippet"]["channelTitle"] : []
                })

        if not any(d["id"] == item["snippet"]["resourceId"]["videoId"] for d in z[item["snippet"]["channelTitle"]]):
            video_info = youtube.videos().list(part='snippet,contentDetails',id=item['snippet']['resourceId']['videoId']).execute()
            z[item["snippet"]["channelTitle"]].append({
                "title": item["snippet"]["title"],
                "kind": "short" if ("#short" in item["snippet"]["title"]) else ("upcoming" if video_info['items'][0]["snippet"]["liveBroadcastContent"] == "upcoming" else "video"),
                "posted": "False",
                "id" : item["snippet"]["resourceId"]["videoId"],
                "liveBroadcastContent": video_info['items'][0]["snippet"]["liveBroadcastContent"]
                })

    json.dump(z, open("video_info.json", "w+"))





ytb_request(ytb_connect(Login.YTB_API_KEY), 20, "UUZEnrtgLG2qb3k7eWjuhacw")