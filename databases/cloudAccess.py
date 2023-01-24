from pymongo import MongoClient
from src.data import Login



def mongoConnect() -> MongoClient:
    return MongoClient(Login.MONGO_URL)


def mongoDisconnect(client: MongoClient):
    client.close()




client = mongoConnect()


database = client["Posts"]
collection = database["Youtube-Uploads"]

cursor = collection.find({})

for document in cursor:
    print(document)


mongoDisconnect(client)