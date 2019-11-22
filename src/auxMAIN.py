from pymongo import MongoClient
from src.auxMONGO import connectCollection
final_db, final_coll = connectCollection('New_York','Final_New_York')
# function that returns video games companies which are at an specified max dist

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