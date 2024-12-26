from machine import Pin
from time import sleep

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(11, Pin.OUT)
led4 = Pin(10, Pin.OUT)

def oneAtATime(timing = .2):
  led1.on()
  sleep(timing)
  led1.off()
  led2.on()
  sleep(timing)
  led2.off()
  led3.on()
  sleep(timing)
  led3.off()
  led4.on()
  sleep(timing)
  led4.off()
  led3.on()
  sleep(timing)
  led3.off()
  led2.on()
  sleep(timing)
  led2.off()

def twoAtATime(timing = .1):
  led1.on()
  sleep(timing)
  led2.on()
  sleep(timing)
  led3.on()
  led1.off()
  sleep(timing)
  led4.on()
  led2.off()
  sleep(timing)
  led3.off()
  sleep(timing)
  led3.on()
  sleep(timing)
  led2.on()
  led4.off()
  sleep(timing)
  led1.on()
  led3.off()
  sleep(timing)
  led2.off()

def twoTwo(timing = .3):
  led1.on()
  led4.on()
  sleep(timing)
  led1.off()
  led4.off()
  led2.on()
  led3.on()
  sleep(timing) 
  led2.off()
  led3.off()

print("Light show GO!")

while True:  
  try:
    twoAtATime()
  except KeyboardInterrupt:
    break

print("Light show STOP!")
  
led1.off()
led2.off()
led3.off()
led4.off()
