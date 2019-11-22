import os
import json
from dotenv import load_dotenv
load_dotenv()

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