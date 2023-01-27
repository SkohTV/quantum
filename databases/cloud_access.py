"""
MongoDB

Posts
	Skoh-Youtube
		Youtube videos / streams / shorts from Skoh's YTB channel

Actions
	Fast
		Actions that should be checked every 10 sec
	Medium
		Actions that should be checked every 1 minute
	Slow
		Actions that should be checked every 1 hour
"""
from pymongo import MongoClient
from src.data import Login




class Atlas:
	"""Posts from Skoh's Youtube channel"""

	def __init__(self, database, collection) -> None:
		self.client = self.connect()
		self.database = self.client[database]
		self.collection = self.database[collection]

	def connect(self):
		"""Connect to MongoDB"""
		return MongoClient(Login.MONGO_URL)

	def disconnect(self):
		"""Close the MongoDB connection"""
		self.client.close()



	def add(self, data, name=None):
		"""Push data to a MongoDB collection"""
		if name is None:
			self.collection.insert_one(data)
		else:
			self.collection.insert_one({name: data})

	def supr(self, data: dict):
		"""Delete data from a MongoDB collection"""
		self.collection.delete_one(data)



	def query(self, data: dict):
		"""Query data from a MongoDB collection"""
		return self.collection.find(data)


	def fetch(self):
		"""Fetch data from a MongoDB collection"""
		cache_database = []
		cursor = self.collection.find({})
		for document in cursor:
			cache_database.append(document)
		return cache_database




#Temp = Atlas("Posts", "Skoh_Youtube")

#Temp.add({"one" : 1})
#Temp.add({"two" : 2})
#Temp.add({"three" : 3})

#Temp.supr(Temp.fetch()[0])

#Temp.disconnect()
