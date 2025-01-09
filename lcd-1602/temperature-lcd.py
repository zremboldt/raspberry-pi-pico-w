from machine import Pin
from lcd1602 import LCD
from time import sleep
from dht import DHT11

lcd = LCD()

button = Pin(15, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.

dataPin = Pin(16, Pin.OUT, Pin.PULL_DOWN)
dht11 = DHT11(dataPin)

isFirstReading = True
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
        lcd.write(0, 0, "Reading")
        lcd.write(0, 1, "from sensor...")
        sleep(3)

      # There's a bug with the DHT11 where the first read is always 0 degrees so this is a workaround.
      if isFirstReading:
        sleep(1)
        dht11.measure()
        isFirstReading = False

      tempCelcius = dht11.temperature()
      humidity = dht11.humidity()
      tempFahrenheit = round(tempCelcius * (9/5) + 32)
      lcd.clear()

    buttonState = button.value()

    # If the button is pressed, toggle the temperature display between Celcius and Fahrenheit.
    if latestButtonState == 1 and buttonState == 0:
      latestButtonState = buttonState
      showFahrenheit = not showFahrenheit
      lcd.clear()
    else:
      latestButtonState = buttonState

    tempString = f'{tempFahrenheit}{chr(223)}F' if showFahrenheit else f'{tempCelcius}{chr(223)}C'

    lcd.write(0, 0, f"Temp: {tempString}")
    lcd.write(0, 1, f"Humidity: {humidity}%")
      
    sleep(0.1)

    if tick == 100:
      tick = 0
    else:
      tick += 1

except KeyboardInterrupt:
  lcd.clear()