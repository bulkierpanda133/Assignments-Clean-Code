# user_interface.py
class UserInterface:
    def __init__(self, weather_fetcher, data_parser):
        self.weather_fetcher = weather_fetcher
        self.data_parser = data_parser

    def get_detailed_forecast(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        return self.data_parser.parse_weather_data(data)

    def display_weather(self, city):
        data = self.weather_fetcher.fetch_weather_data(city)
        if not data:
            return f"Weather data not available for {city}"
        else:
            return self.data_parser.parse_weather_data(data)

    def main(self):
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = self.get_detailed_forecast(city)
            else:
                forecast = self.display_weather(city)
            print(forecast)
