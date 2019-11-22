#Function for getting coordinates from the office DB
def getLocation_offices(office,category):

    longitude = office['offices']['longitude']
    latitude = office['offices']['latitude']
    loc = {'category':category,
    'type':'Point',
    'coordinates':[float(longitude), float(latitude)]}
    return loc