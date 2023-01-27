"""Connect to Youtube API and make requests"""
import googleapiclient.discovery
from pymongo import MongoClient
from databases import cloud_access as cAccess
#from src.data import Login, Socials
from src.logger import logger




def ytb_connect(api_key: str) -> googleapiclient.discovery.Resource:
	"""Create a connection to the Youtube API

	Args:
		API_KEY (str): Given API key located in the .env file

	Returns:
		googleapiclient.discovery.Resource: Youtube object to use for requests
	"""
	api_service_name, api_version, developer_key = "youtube", "v3", api_key
	youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = developer_key)
	return youtube



def ytb_request_playlist(client: MongoClient, youtube: googleapiclient.discovery.Resource, playlist_id: str, max_results = 20, create_empty = False):
	"""Send a request to Youtube API to fetch videos from a playlist

	Args:
		client (MongoClient): MongoDB client to connect to the database.
		youtube (googleapiclient.discovery.Resource): Initialized Youtube object to connect to Youtube API
		playlistId (str): The ID of the playlist to fetch
		maxResults (int, optional): Max number of results to fetch (20 almost every time)
		create_empty (bool, optional): If True, create a new json file with the channel name as key and an empty list as value. Defaults to False.
	"""
	request = youtube.playlistItems().list(
		part='snippet',
		maxResults=max_results,
		playlistId=playlist_id
	)
	response = request.execute()

	mongo_ytb = [] if create_empty else cAccess.fetch(client, "Skoh", "Youtube")["videos"]
	if not create_empty:
		mongo_ytb.reverse()

	for item in response["items"]:
		if not any(d["id"] == item["snippet"]["resourceId"]["videoId"] for d in mongo_ytb):
			video_info = youtube.videos().list(part='snippet,contentDetails',id=item['snippet']['resourceId']['videoId']).execute()
			cAccess.add(client, "Posts", "Skoh-Youtube", {
				"title": item["snippet"]["title"],
				"kind": "short" if ("#short" in item["snippet"]["title"]) else ("upcoming" if video_info['items'][0]["snippet"]["liveBroadcastContent"] == "upcoming" else "video"),
				"posted": "False" if create_empty else "True",
				"id" : item["snippet"]["resourceId"]["videoId"],
				"liveBroadcastContent": video_info['items'][0]["snippet"]["liveBroadcastContent"]
			})

	if not create_empty:
		while len(mongo_ytb) > 20:
			mongo_ytb.pop(0)
			logger("New video")
		mongo_ytb.reverse()
