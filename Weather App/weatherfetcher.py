import requests
api_key="116edb1a16ab7da2c2a4f45f652a0e8e"
lat=28.2639
lon=83.9721
def fetch_weather(api_key,lat,lon):
    url=f"https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude=hourly,daily&appid={api_key}"
    response = requests.get(url)
    
    return response.json()  # Call the json method to get the response data

#examplef
weather_data=fetch_weather(api_key,lat,lon)
print(weather_data)
