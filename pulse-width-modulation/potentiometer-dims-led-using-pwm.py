from machine import Pin, PWM, ADC
from time import sleep

outPin = 11
analogOutPin = PWM(Pin(outPin)) # Set the pin as a PWM output
analogOutPin.freq(1000) # Set the frequency of the PWM signal to 1000Hz. This will blink once per millisecond. Play with the value if desired.
analogOutPin.duty_u16(0) # Set the duty cycle of the PWM signal. This is a 16 bit binary number. 0 is off and 65535 is fully on.

potPin = 28 # Pin for the potentiometer
myPot = ADC(potPin) # Create an Analog to Digital Conversion object

while True:
  binaryMax = 65535
  binaryMin = 0

  potMax = 65535
  potMin = 272

  potValue = myPot.read_u16() # Read the potentiometer value. u16 gives us a 16 bit binary number.

  # Convert the potentiometer value to a number between the binaryMin and the binaryMax
  outputValue = max(0, round((binaryMax - binaryMin) * ((potValue - potMin) / (potMax - potMin)) + binaryMin))
  
  analogOutPin.duty_u16(outputValue)
  print(outputValue)

  sleep(0.1)
