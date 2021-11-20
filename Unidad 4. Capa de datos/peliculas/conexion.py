from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

def connect_mongo():
    client = MongoClient(MONGO_URI)
    return client