from machine import Pin
from time import sleep

led = Pin(0, Pin.OUT)

led.on()
sleep(10)
led.off()
sleep(1)

led.on()
sleep(1)
led.off()
sleep(1)

led.on()
sleep(1)
led.off()
