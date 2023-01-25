from pymongo import MongoClient
from src.data import Login

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



def mongoConnect() -> MongoClient:
    return MongoClient(Login.MONGO_URL)


def mongoDisconnect(client: MongoClient):
    client.close()




# client = mongoConnect()


# database = client["Posts"]
# collection = database["Youtube-Uploads"]
# collection.insert_one({"name": "test"})



# mongoDisconnect(client)




# cursor = collection.find({})
# for document in cursor:
#     print(document)