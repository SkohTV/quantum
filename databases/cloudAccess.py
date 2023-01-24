from pymongo import MongoClient
from src.data import Login



def mongoConnect() -> MongoClient:
    return MongoClient(Login.MONGO_URL)


def mongoDisconnect(client: MongoClient):
    client.close()




client = mongoConnect()


database = client["Posts"]
collection = database["Youtube-Uploads"]
collection.insert_one({"name": "test"})



mongoDisconnect(client)




# cursor = collection.find({})
# for document in cursor:
#     print(document)