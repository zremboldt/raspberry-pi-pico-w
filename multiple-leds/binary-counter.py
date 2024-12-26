from machine import Pin
from time import sleep

led1 = Pin(13, Pin.OUT)
led2 = Pin(12, Pin.OUT)
led3 = Pin(11, Pin.OUT)
led4 = Pin(10, Pin.OUT)

def displayNumber(number, timing = .5):
  if number < 0 or number > 15:
    raise ValueError("Number must be between 0 and 15")
  
  binary_representation = f"{number:04b}"
  
  led1.value(int(binary_representation[3]))
  led2.value(int(binary_representation[2]))
  led3.value(int(binary_representation[1]))
  led4.value(int(binary_representation[0]))
  
  if number == 15:
    sleep(2)
  else:
    sleep(timing)

  led1.off()
  led2.off()
  led3.off()
  led4.off()


print("Count to 15 in binary...")

while True:
  try:
    for i in range(16):
      displayNumber(i)
  except KeyboardInterrupt:
    break

print("Finished.")

led1.off()
led2.off()
led3.off()
led4.off()