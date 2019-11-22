from pymongo import MongoClient
import time
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
    longitude = place['lng']
    latitude = place['lat']
    loc = {
        'category':category,
        'type':'Point',
        'coordinates':[float(longitude), float(latitude)]
    }
    return loc

#Function to perform google queries
def google_query(query):
    API_key = os.getenv('GOOGLE_TOKEN')
    endpoint_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    places = []
    params = {
        'query': query,
        'key': API_key
    }
    res = requests.get(endpoint_url, params = params)
    results =  json.loads(res.content)
    places.extend(results['results'])
    time.sleep(2)
    while "next_page_token" in results:
        params['pagetoken'] = results['next_page_token'],
        res = requests.get(endpoint_url, params = params)
        results = json.loads(res.content)
        places.extend(results['results'])
        time.sleep(2)
    return places

# functions that returns video games companies which are at an specified max dist

def dist(e,max_distance):
    final_db, final_coll = connectCollection('New_York','Final_New_York')
    video_games_locations = list(final_coll.find({'$and':[
        {'category':'Video games companies'},
       {"coordinates": {
         '$near': {
           '$geometry': {
              'type': "Point" ,
              'coordinates': [e['coordinates'][0],e['coordinates'][1]]
           },

           '$maxDistance': max_distance
         }
       }
    }]}))
    return video_games_locations