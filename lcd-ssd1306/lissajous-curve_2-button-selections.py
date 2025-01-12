from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
from time import sleep
import math

buttonGreen = Pin(14, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
buttonBlue = Pin(15, Pin.IN, Pin.PULL_UP) # When setting up a button we can use Pin.PULL_UP to enable the board's internal pull-up resistor rather than setting one up manually.
latestButtonBlueState = 1
latestButtonGreenState = 1

curves = [
  [0.4, 1],
  [1, 2],
  [2, 1],
  [2, 3],
  [1, 3],
  [7, 74],
  [3, 1],
  [3, 5],
  [3, 4],
  [1, 4],
  [1, 1],
  [11, 123]
]

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



def updateCurve(direction):
  global currentCurve
  global drawPointsInSucession

  if direction == "increment":
    if currentCurve == len(curves) - 1:
      currentCurve = 0
    else:
      currentCurve += 1

  if direction == "decrement":
    if currentCurve == 0:
      currentCurve = len(curves) - 1
    else:
      currentCurve -= 1

  print("\r", f"Current curve: {curves[currentCurve]}", end=' ')
  drawPointsInSucession = True



# Initialize the I2C bus
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

tick = 0
drawPointsInSucession = False
currentCurve = 0

while True:
  display.fill(0)

  xCenter = 64
  yCenter = 32
  xRadius = 52
  yRadius = 24

  handleButtonPress("blue", lambda: updateCurve("decrement"))
  handleButtonPress("green", lambda: updateCurve("increment"))
    
  for i in range(0, 360, 2):
    x = int(xCenter + xRadius * math.cos(math.radians(i * curves[currentCurve][0])))
    y = int(yCenter + yRadius * math.sin(math.radians(i * curves[currentCurve][1]) + (tick * 0.05)))
    display.pixel(x, y, 1)
  
    if i != 358 and drawPointsInSucession:
      if i % 10 == 0: # Run show fn for every 10th pixel (makes drawing faster).
        display.show()
    else:
      drawPointsInSucession = False
      
  display.show()
  tick += 1


