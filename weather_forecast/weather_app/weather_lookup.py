import requests
from datetime import datetime

def get_weather_forecast(api_key, lat, lon, time_input):
    base_url = "http://api.openweathermap.org/data/2.5/forecast"
    params = {
        'lat': lat,
        'lon': lon,
        'appid': api_key,
    }

    response = requests.get(base_url, params=params)

    if response.status_code == 200:
        weather_data = response.json()

        
        if 'list' in weather_data:
            for item in weather_data['list']:
                
                item_datetime = datetime.strptime(item['dt_txt'], '%Y-%m-%d %H:%M:%S')

                
                input_datetime = datetime.strptime(time_input, '%Y-%m-%dT%H:%M')

                
                if item_datetime == input_datetime:
                    return item

            
            return f"No weather data available for the specified time: {time_input}"

        else:
            return f"Unexpected response format. 'list' key not found in response data."

    else:
        return f"Failed to fetch weather data. Status code: {response.status_code}"


