import requests
from pprint import pprint

space_url = 'http://api.open-notify.org/iss-now.json'
my_key = open('google_api_key.txt', 'r').read()

def get_json(url, data = None):
    request = requests.get(url, params=None)
    response = request.json()
    return response

def get_station(url):
    space_response = get_json(url)
    for key, value in space_response['iss_position'].items():
        if key == 'longitude':
            latitude = value
        if key == 'latitude':
            longitude = value
    return latitude, longitude

def get_location(url):
    response = get_json(url)
    if response['status'] == 'ZERO_RESULTS':
        try:
            while response['status'] != 'OK':
                print(response['status'])
                response = get_json(url)
        except Exception as error:
            print(error)
    return response

latitude, longitude = get_station(space_url)
google_url = 'https://maps.googleapis.com/maps/api/geocode/json?latlng={lat},{long}&key={key}'.format(lat=latitude, long=longitude, key=my_key)
get_loc = get_location(google_url)
pprint(get_loc)

print('''The International Space Station is located:
Latitude: {lat}
Longtitude: {long}
'''.format(lat=latitude, long=longitude))

for loc in get_loc['results']:
    print(loc['formatted_address'])