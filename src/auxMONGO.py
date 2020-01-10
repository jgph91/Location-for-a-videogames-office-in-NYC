from pymongo import MongoClient

def connectCollection(database, collection):
    '''Function for connecting to MongoDB'''

    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll