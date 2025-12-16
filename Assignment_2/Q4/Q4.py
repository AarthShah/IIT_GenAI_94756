import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_key=os.getenv('OpenWeather_API_key')

City_name=input("Enter city name: ")

url=f"https://api.openweathermap.org/data/2.5/weather?q={City_name}&appid={API_key}"

response=requests.get(url)
data=response.json()

#print(data)
print(f"Weather in {City_name}: {data['main']['temp']} K , Humidity: {data['main']['humidity']}% , Weather Description: {data['weather'][0]['description']}")

