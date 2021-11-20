from pymongo import MongoClient

MONGO_URI = "mongodb://localhost"

def get_database():
    database='pelicula'
    client = MongoClient(MONGO_URI)
    db = client[database]
    return db