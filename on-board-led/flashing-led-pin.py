from machine import Pin
from time import sleep

ledOut = Pin('LED', Pin.OUT) # Getting the pin on the board called LED and sending a message OUT to it. Then setting that to a variable.

# 1 is on, 0 is off.
# ledOut.value(0)

while True:
    ledOut.toggle()
    sleep(2)