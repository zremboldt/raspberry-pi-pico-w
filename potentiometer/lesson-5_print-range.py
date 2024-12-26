import machine
from time import sleep

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

  print(round(voltage)) # Print the value to the console
  sleep(0.5)
