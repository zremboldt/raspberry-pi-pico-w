from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

# Initialize the I2C bus
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

display.text("Hello, World!", 0, 0)
display.hline(0, 12, 128, 1)
display.show()

# display.poweroff()