from machine import Pin
from time import sleep

redLed = Pin(15, Pin.OUT)

def blinkSequence(blinkCount, blinkLength):
  for _ in range(blinkCount):
    redLed.on()
    sleep(blinkLength)
    redLed.off()
    sleep(0.2)

def sos():
  for i in range(3):
    if i % 2 == 0:
      blinkSequence(3, .15)
    else:
      blinkSequence(3, .6)

print("Sending out an SOS...")

while True:
  try:
    sos()
    sleep(1.5)
  except KeyboardInterrupt:
    break

print("Finished.")