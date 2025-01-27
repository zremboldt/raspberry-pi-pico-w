# Open Weather API: https://openweathermap.org/current
import network
from time import sleep, localtime
import urequests # This library allows us to make requests to API's over the internet
import secrets

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore

while not wifi.isconnected():
  print("Connecting...")
  sleep(1)

print(f"Connected! \n")

try:
  res = urequests.get(f"http://api.openweathermap.org/data/2.5/weather?zip=67223,us&appid={secrets.openWeatherApiKey}&units=imperial").json() # type: ignore

  city_name = res['name']
  temperature = round(res['main']['temp'])
  feels_like = round(res['main']['feels_like'])
  description = res['weather'][0]['description']
  humidity = res['main']['humidity']
  wind_speed = round(res['wind']['speed'])
  sunriseData = localtime(res['sys']['sunrise'] + res['timezone'])
  sunsetData = localtime(res['sys']['sunset'] + res['timezone'])
  sunrise = f"{sunriseData[3]}:{sunriseData[4]}"
  sunset = f"{sunsetData[3] - 12}:{sunsetData[4]}"

  print(f"Location ...... {city_name}, KS")
  print(f"Temperature ... {temperature}F")
  print(f"Feels like .... {feels_like}F")
  print(f"Description ... {description}")
  print(f"Humidity ...... {humidity}%")
  print(f"Wind Speed .... {wind_speed} mph")
  print(f"Sunrise ....... {sunrise} AM")
  print(f"Sunset ........ {sunset} PM")

except Exception as e:
  print("Error:", e)
