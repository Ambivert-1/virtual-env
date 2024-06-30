def parse_weather(data):
    city=data['location']['name']
    temperature=data['current']['temp_c']
    condition=data['current']['condition']['text']


    weather_info=f"Weather in {city}:{temperature}°C, {condition}"
    return(weather_info)