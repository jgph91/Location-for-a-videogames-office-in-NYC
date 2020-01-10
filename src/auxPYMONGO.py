def getLocation_offices(office,category):
    '''Function for getting coordinates from the office DB'''

    longitude = office['offices']['longitude']
    latitude = office['offices']['latitude']
    loc = {'category':category,
    'type':'Point',
    'coordinates':[float(longitude), float(latitude)]}
    return loc