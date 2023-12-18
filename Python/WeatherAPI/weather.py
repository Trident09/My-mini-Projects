import requests

API_KEY = "2c3a6a50789c94474a933a43ff6cd1c1"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

city = input("Enter a city name: ")
request_url = f"{BASE_URL}?appid={API_KEY}&q={city}"
response = requests.get(request_url)

if response.status_code == 200:
    data = response.json()
    weather = data['weather'][0]['description']
    print(weather)
    temperature = round(data['main']['temp'] - 273.15, 2)
    print(f"Temperature: {temperature}°C")
    humidity = data['main']['humidity']
    print(f"Humidity: {humidity}%")
    wind_speed = data['wind']['speed']
    print(f"Wind Speed: {wind_speed}m/s")
else:
    print("Error in retrieving data")