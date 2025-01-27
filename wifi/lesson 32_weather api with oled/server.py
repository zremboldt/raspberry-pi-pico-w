# Open Weather API: https://openweathermap.org/current
import network
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
from time import sleep, localtime
import urequests # This library allows us to make requests to API's over the internet
import secrets

# LED setup
ledRed = Pin(14, Pin.OUT)
ledBlue = Pin(15, Pin.OUT)

#---------------------------------
### Display setup
#---------------------------------

# Initialize the I2C bus (for the OLED display)
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

def oledPrint(message):
  display.fill(0)
  display.text(message, 0, 0)
  display.show()

#---------------------------------
# WiFi Setup
#---------------------------------

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore

while not wifi.isconnected():
  oledPrint("Connecting...")
  sleep(1)

oledPrint("Connected!")

#---------------------------------
# Main
#---------------------------------

WEATHER_API_URI = f"http://api.openweathermap.org/data/2.5/weather?zip=67223,us&appid={secrets.openWeatherApiKey}&units=imperial" # type: ignore

res = None
tick = 0

try:
  res = urequests.get(WEATHER_API_URI).json()

  while True:
    # refetch the weather data every 20 minutes
    if tick == 60 * 20:
      print("Refetching weather data...")
      res = urequests.get(WEATHER_API_URI).json()
      tick = 0

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

    if temperature > 70:
      ledRed.value(1)
      ledBlue.value(0)
    else:
      ledRed.value(0)
      ledBlue.value(1)

    display.fill(0)
    display.text(f"Weather in", 0, 0)
    display.text(f"{city_name}", 0, 15)
    display.text(f"Temp: {temperature}F", 0, 30)
    display.text(f"Feels like: {feels_like}F", 0, 45)
    display.show()

    sleep(5)

    display.fill(0)
    display.text(f"Humidity: {humidity}%", 0, 0)
    display.text(f"Wind: {wind_speed} mph", 0, 15)
    display.text(f"Sunrise: {sunrise} AM", 0, 30)
    display.text(f"Sunset: {sunset} PM", 0, 45)
    display.show()

    sleep(5)
    tick += 10

except KeyboardInterrupt:
  display.poweroff()
  ledRed.value(0)
  ledBlue.value(0)
