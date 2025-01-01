from machine import Pin, PWM
from time import sleep

buttonRed = Pin(7, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
buttonGreen = Pin(9, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
buttonBlue = Pin(10, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.

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

latestButtonRedState = 1
latestButtonGreenState = 1
latestButtonBlueState = 1

try:
  while True:
    buttonRedState = buttonRed.value()
    buttonGreenState = buttonGreen.value()
    buttonBlueState = buttonBlue.value()

    if buttonRedState != latestButtonRedState:
      latestButtonRedState = buttonRedState
      setColor(100, 0, 0)

    if buttonGreenState != latestButtonGreenState:
      latestButtonGreenState = buttonGreenState
      setColor(0, 100, 0)

    if buttonBlueState != latestButtonBlueState:
      latestButtonBlueState = buttonBlueState
      setColor(0, 0, 100)

    sleep(0.1)

except KeyboardInterrupt:
  setColor(0, 0, 0)
