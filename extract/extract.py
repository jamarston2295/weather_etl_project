import requests

def fetch_weather_data(city):
    api_key = "demo"  # Replace with your real API key
    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    raise Exception(f"Failed to fetch data: {response.status_code}")
