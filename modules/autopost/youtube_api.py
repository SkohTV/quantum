"""Connect to Youtube API and make requests"""
import googleapiclient.discovery
#from src.data import Login, Socials
from src.logger import logger
from databases.cloud_access import Atlas




def ytb_connect(api_key: str) -> googleapiclient.discovery.Resource:
	"""Create a connection to the Youtube API"""
	api_service_name, api_version, developer_key = "youtube", "v3", api_key
	youtube = googleapiclient.discovery.build(api_service_name, api_version, developerKey = developer_key)
	return youtube



def ytb_request_playlist(client: Atlas, youtube: googleapiclient.discovery.Resource, playlist_id: str, max_results = 5, create_empty = False) -> list:
	"""Send a request to Youtube API to fetch videos from a playlist

	Args:
		client (Atlas): MongoDB client to connect to the database
		youtube (googleapiclient.discovery.Resource): Initialized Youtube object to connect to Youtube API
		playlistId (str): The ID of the playlist to fetch
		maxResults (int, optional): Max number of results to fetch (20 almost every time)
		create_empty (bool, optional): If True, create a new json file with the channel name as key and an empty list as value (defaults to False)

	Returns:
		list: List of all new videos
	"""
	request = youtube.playlistItems().list(
		part='snippet',
		maxResults= 19 if create_empty else	max_results,
		playlistId=playlist_id
	)
	response = request.execute()
	mongo_ytb = [] if create_empty else client.fetch()
	if not create_empty:
		mongo_ytb.reverse()

	new_data = []
	#print(mongo_ytb)

	for item in response["items"]:
		if not any(d["id"] == item["snippet"]["resourceId"]["videoId"] for d in mongo_ytb):
			logger(f"New video : {item['snippet']['title']}")
			video_info = youtube.videos().list(part='snippet,contentDetails',id=item['snippet']['resourceId']['videoId']).execute()
			new_data.append({
				"title": item["snippet"]["title"],
				"kind": "short" if ("#short" in item["snippet"]["title"]) else ("upcoming" if video_info['items'][0]["snippet"]["liveBroadcastContent"] == "upcoming" else "video"),
				"posted": "False" if create_empty else "True",
				"id" : item["snippet"]["resourceId"]["videoId"],
				"liveBroadcastContent": video_info['items'][0]["snippet"]["liveBroadcastContent"]
			})

	if create_empty:
		new_data.reverse()

	for i in new_data:
		client.add(i)

	if not create_empty:
		while len(mongo_ytb) > 20:
			client.supr(client.fetch()[0])
			mongo_ytb.pop(0)
			logger("Video popped of the database")

	return new_data


# TESTS


#temp = Atlas("Posts", "Skoh_Youtube")

#try:
#	for i in range(100):
#		temp.supr(temp.fetch()[0])
#except IndexError:
#	pass

#yt.ytb_request_playlist(temp, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb, create_empty=True)
#yt.ytb_request_playlist(temp, yt.ytb_connect(Login.YTB_API_KEY), Socials.posts_skoh_ytb)
#temp.supr(temp.fetch()[0])

#temp.disconnect()
