from machine import Pin
from time import sleep

led1 = Pin(15, Pin.OUT)
led2 = Pin(14, Pin.OUT)
led3 = Pin(13, Pin.OUT)
led4 = Pin(12, Pin.OUT)
led5 = Pin(11, Pin.OUT)

def slideRight(timing = .1):
  led1.on()
  sleep(timing)

  led2.on()
  sleep(timing)
  led1.off()

  led3.on()
  sleep(timing)
  led2.off()

  led4.on()
  sleep(timing)
  led3.off()

  led5.on()
  sleep(timing)
  led4.off()

  sleep(timing)
  led5.off()


def slideLeft(timing = .1):
  led5.on()
  sleep(timing)

  led4.on()
  sleep(timing)
  led5.off()

  led3.on()
  sleep(timing)
  led4.off()

  led2.on()
  sleep(timing)
  led3.off()

  led1.on()
  sleep(timing)
  led2.off()

  sleep(timing)
  led1.off()

def flash(led, timing = .03):
  led.on()
  sleep(timing)
  led.off()

def splatterRight():
  flash(led1)
  flash(led4)
  flash(led2)
  flash(led5)
  flash(led4)
  flash(led1)
  flash(led3)
  flash(led5)

def splatterLeft():
  flash(led5)
  flash(led3)
  flash(led1)
  flash(led4)
  flash(led5)
  flash(led2)
  flash(led4)
  flash(led1)

print("Light show GO!")

while True:  
  try:
    slideRight()
    slideLeft()
    slideRight()
    splatterRight()
    slideLeft()
    slideRight()
    slideLeft()
    splatterLeft()
  except KeyboardInterrupt:
    break

print("Light show STOP!")
  
led1.off()
led2.off()
led3.off()
led4.off()
led5.off()
