from pymongo import MongoClient
import os
import json
import requests
from dotenv import load_dotenv
load_dotenv()

# Function for connecting to MongoDB
def connectCollection(database, collection):
    client = MongoClient()
    db = client[database]
    coll = db[collection]
    return db, coll

#Function for getting coordinates from the office DB
def getLocation_offices(office,category):

    longitude = office['offices']['longitude']
    latitude = office['offices']['latitude']
    loc = {'category':category,
    'type':'Point',
    'coordinates':[float(longitude), float(latitude)]}
    return loc

#Function for getting coordinates from the Gmaps API
def getLocation_API(place,category):
    longitude = place['location']['lng']
    latitude = place['location']['lat']
    loc = {
        'category':category,
        'type':'Point',
        'coordinates':[float(longitude), float(latitude)]
    }
    return loc

#Function to perform google queries
def google_query(query):
    coords = []
    api_key = os.getenv("GOOGLE_TOKEN")
    url = "https://maps.googleapis.com/maps/api/place/textsearch/json?"
    r = requests.get(url + 'query=' + query + '&key=' + api_key) 
    x = r.json() 
    y = x['results'] 
    for i in range(len(y)): 
        coords.append(( y[i]['geometry']))
    return coords