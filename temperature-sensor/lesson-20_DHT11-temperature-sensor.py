from machine import Pin
from time import sleep
from dht import DHT11

dataPin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
dht11 = DHT11(dataPin)

try:
  while True:
    try:
      dht11.measure() # This method doesn't return anything, it simply initiates the measurement.
    except:
      print("Reading from sensor...")
      sleep(3)

    tempCelcius = dht11.temperature()
    humidity = dht11.humidity()

    tempFahrenheit = round(tempCelcius * (9/5) + 32)

    print("\r", f'Temperature: {tempFahrenheit}F, Humidity: {humidity}%', end='')

    sleep(3)

except KeyboardInterrupt:
  print("Shutting down...")