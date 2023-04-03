
import redis
import os
import json



class Youtube:

	def clear_db():
		pass


	def is_first():
		pass


	async def is_already_db(value):
		r = redis.from_url(os.environ.get("REDIS_URI"))
		res = r.get('YTB_Posted')
		db_posted = [i["video_ID"] for i in json.loads(res)] if res != None else []
		return value in db_posted


	def add_database(results, videoFormat, doSend):
		redis.from_url(os.environ.get("REDIS_URI"))
		pass
	#! Stopped here atm

