from machine import Pin, PWM

outPin = 11
analogOutPin = PWM(Pin(outPin)) # Set the pin as a PWM output
analogOutPin.freq(1000) # Set the frequency of the PWM signal to 1000Hz. This will blink once per millisecond. Play with the value if desired.
analogOutPin.duty_u16(0) # Set the duty cycle of the PWM signal. This is a 16 bit binary number. 0 is off and 65535 is fully on.

while True:
  binaryMax = 65550
  humanReadableMax = 100 # We want to convert the binary value to a number between 0 and 100
  
  userInput = int(input("Enter a number between 0 and 100: "))

  outputNumber = round((binaryMax / humanReadableMax) * userInput)
  analogOutPin.duty_u16(outputNumber)
  print(outputNumber)
