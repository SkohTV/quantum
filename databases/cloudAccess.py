from pymongo import MongoClient
from src.data import Login


client = MongoClient(Login.MONGO_URL)
database = client["Posts"]
collection = database["Youtube-Uploads"]

cursor = collection.find({})

for document in cursor:
    print(document)


client.close()

print("done")