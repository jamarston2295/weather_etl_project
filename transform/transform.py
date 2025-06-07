def transform_weather_data(data):
    return {
        "city": data["location"]["name"],
        "temperature": data["current"]["temp_c"],
        "condition": data["current"]["condition"]["text"]
    }
