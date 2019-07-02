import json
import requests

key = '871739dba041ff5e28527b05b9077d15' # Gregory

# key = 'cd1046ee98eec3e0f87367a0fbfcb817' # Cristina

def find_weather(time):
    """Returns weather data as a binary (0 = not rain, 1 = rain) from Berlin given a specified date"""
    latitude = "52.520008"
    longitude =  "13.4050"
    location = 'Berlin'
    search_limit = '30'
    base_url = 'https://api.darksky.net/'
    url = base_url +'forecast/' + key + '/'+ latitude + ',' + longitude 
    headers = {'Authorization': 'Bearer {}'.format(key),}
    url_params = {'latitude': latitude, 'longitude': longitude, 'location': location, 'time': time, 'limit': search_limit}
    response = requests.get(url, headers = headers, params = url_params)
    data = json.loads(response.text)
    if ['daily']['data'][0]['icon'] == 'rain':
        return 1
    else:
        return 0