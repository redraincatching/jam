from datetime import datetime, timedelta
import requests
import json


city_coords = {
    'galway': ('53.270668', '-9.056790'),
    'oslo': ('59.913868', '10.752245'),
    'london': ('51.507351', '-0.127758')
}

measurements = {
    'temperature': 'temperature_2m_max',
    'rain': 'rain_sum',
    'windspeed': 'windspeed_10m_max'
}

desc = {
    'temperature': 'highest recorded temperature',
    'rain': 'total rainfall recorded',
    'windspeed': 'highest windspeed recorded'
}

units = {
    'temperature': 'degrees celsius',
    'rain': 'mm',
    'windspeed': 'km/h'
}

def weather(message):
    message = message.lower()

    # Let's build the API call!

    # For challenge 3.1, you'll need to get the longitude and latitude for Galway
    # and put them in the params below.

    # For 3.2, looks like you'll need a mapping of cities to coordinates. Check out
    # city_coords above, and wire it up to solve this challenge!

    # 3.3 doesn't really introcude any new concepts. You're on your own!

    date_now = (datetime.now() - timedelta(days=-1)).strftime('%Y-%m-%d')
    daily_params = ['temperature_2m_max', 'rain_sum', 'windspeed_10m_max']
    params = {
        'latitude': 0,  # You need to update this
        'longitude': 0, # ... and this
        'start_date': date_now,
        'end_date': date_now,
        'timezone': 'GMT',
        'daily': daily_params
    }

    # actually, works better out of the if, if it's a default
    location = "galway"
    measurement = "temperature"

    # part 1: weather with no input, check weather in galway
    # ['daily']['time'][0]
    # if (len(message) == 0):
    #     location = "galway"
    # part 2: assume it's an allowed city
    if (len(message) > 0):
        # so check if a measurement was given
        if (message.__contains__(' ')):
            location, measurement = message.split(" ")
            for m in measurements:
                if measurement == m:
                    measurement = m
        
        for city in city_coords:
            if location == city:
                location = location

                
    params["latitude"] = city_coords[location][0]
    params["longitude"] = city_coords[location][1]


    # This makes a request to the weather API with the above info.
    response = requests.get('https://api.open-meteo.com/v1/forecast', params=params).json()

   
    # Let's print the response. Look out for this in your terminal, you'll need to pull
    # out the bits of information that are relevant to the command used.
    # print(json.dumps(response, indent=4))


    output = "yesterday, the " + desc[measurement] + " in " + location + " was " + str(response['daily'][measurements[measurement]][0]) + " " + units[measurement] +"."

    # This is a placeholder response to show how to drill into the info that you're interested in.
    return output
