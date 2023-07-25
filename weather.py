import requests

API_URL = "https://samples.openweathermap.org/data/2.5/forecast/hourly?q=London,us&appid=b6907d289e10d714a6e88b30761fae22"

def get_weather_data():
    response = requests.get(API_URL)
    if response.status_code == 200:
        return response.json()["list"]
    else:
        print("Error fetching weather data.")
        return []

def get_weather_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if date in entry["dt_txt"]:
            return entry["main"]["temp"]
    return None

def get_wind_speed_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if date in entry["dt_txt"]:
            return entry["wind"]["speed"]
    return None

def get_pressure_by_date(date):
    weather_data = get_weather_data()
    for entry in weather_data:
        if date in entry["dt_txt"]:
            return entry["main"]["pressure"]
    return None

def main():
    while True:
        print("1. Get weather")
        print("2. Get Wind Speed")
        print("3. Get Pressure")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            temp = get_weather_by_date(date)
            if temp is not None:
                print(f"The temperature on {date} is {temp} Kelvin.")
            else:
                print("Weather data not found for the input date.")
        elif choice == "2":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            wind_speed = get_wind_speed_by_date(date)
            if wind_speed is not None:
                print(f"The wind speed on {date} is {wind_speed} m/s.")
            else:
                print("Weather data not found for the input date.")
        elif choice == "3":
            date = input("Enter the date (YYYY-MM-DD HH:MM:SS format): ")
            pressure = get_pressure_by_date(date)
            if pressure is not None:
                print(f"The pressure on {date} is {pressure} hPa.")
            else:
                print("Weather data not found for the input date.")
        elif choice == "0":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
