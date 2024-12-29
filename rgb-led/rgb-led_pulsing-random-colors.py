from machine import Pin, PWM
from time import sleep
import random

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


colors = ['magenta', 'red', 'cyan', 'green', 'blue',]

i = 0
color = 'red'

try:
  while True:
    if i == 0:
      # Choose next color in the list. Not a random color.
      color = colors[colors.index(color) + 1] if colors.index(color) < len(colors) - 1 else colors[0]
      print(color)

    if i < 100:
      if color == 'red':
        setColor(i, 0, 0)
      elif color == 'green':
        setColor(0, i, 0)
      elif color == 'blue':
        setColor(0, 0, i)
      elif color == 'cyan':
        setColor(0, i, i)
      elif color == 'magenta':
        setColor(i, 0, i)
      elif color == 'white':
        setColor(i, i, i)
    elif i < 200:
      if color == 'red':
        setColor(200 - i, 0, 0)
      elif color == 'green':
        setColor(0, 200 - i, 0)
      elif color == 'blue':
        setColor(0, 0, 200 - i)
      elif color == 'cyan':
        setColor(0, 200 - i, 200 - i)
      elif color == 'magenta':
        setColor(200 - i, 0, 200 - i)
      elif color == 'white':
        setColor(200 - i, 200 - i, 200 - i)
    
    if i == 200:
      i = 0
    else:
      i += 1

    sleep(0.01)

except KeyboardInterrupt:
  setColor(0, 0, 0)
