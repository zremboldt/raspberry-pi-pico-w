from machine import Pin
from time import sleep

redLed = Pin(15, Pin.OUT)

def flashSequence(flashLength):
    x = 3
    
    while x > 0:
        redLed.value(1)
        sleep(flashLength)
        redLed.value(0)
        sleep(.2)
        
        x -= 1


while True:
    flashSequence(.1)
    flashSequence(.6)
    flashSequence(.1)
    
    redLed.value(0)
    sleep(2)
