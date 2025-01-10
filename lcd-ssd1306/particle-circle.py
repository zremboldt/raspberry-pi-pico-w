from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
from time import sleep
import math

# Initialize the I2C bus
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

tick = 0

while True:
  display.fill(0)
  
  xCenter = 64
  yCenter = 32
  circleRadius = 30

  def drawParticle(radius, instance):
    x = int(xCenter + radius * math.cos(math.radians(instance)))
    y = int(yCenter + radius * math.sin(math.radians(instance)))
    display.pixel(x, y, 1)

  for i in range(0, 360, 20):
    for j in range(0, 6):
      drawParticle(circleRadius - j, i + tick)

  sleep(0.01)
  display.show()

  if tick <= 18:
    tick += 1
  else:
    tick = 0

