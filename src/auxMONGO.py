from pymongo import MongoClient

# Function for connecting to MongoDB
def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll