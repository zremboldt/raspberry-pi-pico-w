from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
from time import sleep
import math

# Blue 1 Green 2 completes the homework.

# Cool values when transformerY is 5
# transformerX = 34.1 transformerY = 5
# transformerX = 1 transformerY = 5
# transformerX = 2.5 transformerY = 5
# transformerX = 123 transformerY = 5
# transformerX = 304 transformerY = 5
# transformerX = 309 transformerY = 5
# transformerX = 3 transformerY = 5
# transformerX = 55.5 transformerY = 5
# transformerX = 22 transformerY = 23
# transformerX = 6 transformerY = 64
# transformerX = 7 transformerY = 74
# transformerX = 7 transformerY = 76 THIS IS A GOOD ONE!
# transformerX = 11 transformerY = 112
# transformerX = 11 transformerY = 113
# transformerX = 11 transformerY = 123
# transformerX = 8 transformerY = 82

buttonGreen = Pin(14, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
buttonBlue = Pin(15, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
latestButtonBlueState = 1
latestButtonGreenState = 1

def handleButtonPress(color, callback=None):
  global latestButtonBlueState
  global latestButtonGreenState
  
  if color == "blue":
    buttonBlueState = buttonBlue.value()

    if latestButtonBlueState == 1 and buttonBlueState == 0:
      if callback:
        callback()

    latestButtonBlueState = buttonBlueState
  
  if color == "green":
    buttonGreenState = buttonGreen.value()

    if latestButtonGreenState == 1 and buttonGreenState == 0:
      if callback:
        callback()

    latestButtonGreenState = buttonGreenState

def increment_transformer(transformer):
  global transformerX
  global transformerY
  global drawEachPoint

  if transformer == "X":
    if transformerX < 1:
      transformerX = 1
    else:
      transformerX += 1
  
  if transformer == "Y":
      transformerY += 1

  print("\r", f"Blue: {transformerX}, Green: {transformerY}", end=' ')
  drawEachPoint = True

# Initialize the I2C bus
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

tick = 0
drawEachPoint = False
transformerX = 0.3
transformerY = 1

while True:
  display.fill(0)

  xCenter = 64
  yCenter = 32
  circleRadius = 20

  handleButtonPress("blue", lambda: increment_transformer("X"))
  handleButtonPress("green", lambda: increment_transformer("Y"))
    
  for i in range(0, 360, 2):
    x = int(xCenter + circleRadius * math.cos(math.radians(i * transformerX) + (tick * 0.05)) * 2.5)
    y = int(yCenter + circleRadius * math.sin(math.radians(i * transformerY) + (tick * 0.05)))
    display.pixel(x, y, 1)

    if i != 358 and drawEachPoint:
      display.show() # Show the drawing of each pixel in succession.
    else:
      drawEachPoint = False
      
  display.show()
  tick += 1


