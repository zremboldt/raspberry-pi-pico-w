import machine
from time import sleep

led1 = machine.Pin(13, machine.Pin.OUT)
led2 = machine.Pin(12, machine.Pin.OUT)
led3 = machine.Pin(11, machine.Pin.OUT)
led4 = machine.Pin(10, machine.Pin.OUT)

potPin = 28 # Pin for the potentiometer
myPot = machine.ADC(potPin) # Create an Analog to Digital Conversion object

# We want to make constant readings of the potentiometer so we use a loop
while True:
  potValue = myPot.read_u16() # Read the potentiometer value. u16 gives us a 16 bit binary number.
  
  binaryMax = 65230
  binaryMin = 272

  # desiredMax = 3.3 # We want to convert the binary value to a voltage between 0 and 3.3V
  desiredMax = 100 # We want to convert the binary value to a number between 0 and 100

  # Useful formula for converting one number range to another
  voltage = (desiredMax / binaryMax) * potValue - (binaryMin * desiredMax / binaryMax) # Convert the binary range to our desired range

  if voltage < 20:
    led1.off()
    led2.off()
    led3.off()
    led4.off()
  elif voltage < 50:
    led1.on()
    led2.off()
    led3.off()
    led4.off()
  elif voltage < 75:
    led1.on()
    led2.on()
    led3.off()
    led4.off()
  elif voltage < 95:
    led1.on()
    led2.on()
    led3.on()
    led4.off()
  else:
    led1.on()
    led2.on()
    led3.on()
    led4.on()

  print(round(voltage)) # Print the value to the console
  sleep(0.2)
