from extract.extract import fetch_weather_data
from transform.transform import transform_weather_data
from load.load import load_to_csv

if __name__ == "__main__":
    raw_data = fetch_weather_data("London")
    transformed = transform_weather_data(raw_data)
    load_to_csv(transformed)
