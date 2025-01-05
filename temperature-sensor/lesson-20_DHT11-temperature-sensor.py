from machine import Pin
from time import sleep
from dht import DHT11

button = Pin(15, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.

dataPin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
dht11 = DHT11(dataPin)

tick = 0
latestButtonState = 1
showFahrenheit = False
tempCelcius = None
humidity = None
tempFahrenheit = None

try:
  while True:
    # Gather data from the sensor every 10 seconds.
    if tick == 0:
      try:
        dht11.measure() # This method doesn't return anything, it simply initiates the measurement.
      except:
        print("Reading from sensor...")
        sleep(3)

      tempCelcius = dht11.temperature()
      humidity = dht11.humidity()
      tempFahrenheit = round(tempCelcius * (9/5) + 32)

    buttonState = button.value()

    # If the button is pressed, toggle the temperature display between Celcius and Fahrenheit.
    if latestButtonState == 1 and buttonState == 0:
      latestButtonState = buttonState
      showFahrenheit = not showFahrenheit
    else:
      latestButtonState = buttonState

    if showFahrenheit:
      print("\r", f'Temperature: {tempFahrenheit}F, Humidity: {humidity}%', end='')
    else:
      print("\r", f'Temperature: {tempCelcius}C, Humidity: {humidity}%', end='')
      
    sleep(0.1)

    if tick == 100:
      tick = 0
    else:
      tick += 1

except KeyboardInterrupt:
  print("Shutting down...")