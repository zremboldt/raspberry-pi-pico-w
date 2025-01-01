from machine import Pin, PWM
from time import sleep

button = Pin(10, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.

ledRed = PWM(Pin(13))
ledGreen = PWM(Pin(12))
ledBlue = PWM(Pin(11))

ledRed.freq(1000)
ledGreen.freq(1000)
ledBlue.freq(1000)

binaryMax = 65535
humanReadableMax = 100
getBinaryValue = lambda value: round((binaryMax / humanReadableMax) * value)

def setColor(red, green, blue):
  ledRed.duty_u16(getBinaryValue(red))
  ledGreen.duty_u16(getBinaryValue(green))
  ledBlue.duty_u16(getBinaryValue(blue))


colors = ['red', 'magenta', 'green', 'yellow', 'orange', 'blue', 'pink', 'white', 'off']
color = 'off'

latestButtonState = 1

try:
  while True:
    buttonState = button.value()

    if buttonState != latestButtonState:
      print(buttonState)
      latestButtonState = buttonState
    
      if buttonState == 0:
        color = colors[colors.index(color) + 1] if colors.index(color) < len(colors) - 1 else colors[0]

      if color == 'red':
        setColor(100, 0, 0)
      elif color == 'green':
        setColor(0, 100, 0)
      elif color == 'magenta':
        setColor(100, 0, 100)
      elif color == 'blue':
        setColor(0, 0, 100)
      elif color == 'yellow':
        setColor(100, 30, 0)
      elif color == 'orange':
        setColor(100, 5, 0)
      elif color == 'pink':
        setColor(100, 0, 30)
      elif color == 'white':
        setColor(100, 100, 100)
      elif color == 'off':
        setColor(0, 0, 0)

    sleep(0.1)

except KeyboardInterrupt:
  setColor(0, 0, 0)
