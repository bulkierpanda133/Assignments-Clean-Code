# main.py
from weather_fetcher import WeatherDataFetcher
from data_parser import DataParser
from user_interface import UserInterface

if __name__ == "__main__":
    weather_fetcher = WeatherDataFetcher()
    data_parser = DataParser()
    user_interface = UserInterface(weather_fetcher, data_parser)
    user_interface.main()
