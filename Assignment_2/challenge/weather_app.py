from weather_api import Weather_in_city
import time

def welcome_message():
    mess="Welcome to the Weather App! You can get the current weather information for any city." 
    for i in mess.split():
        print(i, end=" ", flush=True)
        time.sleep(0.15)

    get_city()

def get_city():
    city_name=input("\nPlease enter the city name: ")
    weather_info=Weather_in_city(city_name)
    print(weather_info)

welcome_message()

while True:
    more_info=input("Do you want to check the weather for another city? (yes/no): ").strip().lower()
    if more_info == 'yes':
        get_city()
    elif more_info == 'no':
        print("Thank you for using the Weather App. Goodbye!")
        break
    else:
        print("Invalid input. Please enter 'yes' or 'no'.")