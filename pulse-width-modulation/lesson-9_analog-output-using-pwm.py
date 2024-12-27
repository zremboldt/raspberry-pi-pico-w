from machine import Pin, PWM
from time import sleep

outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
  binaryMax = 65550 
  desiredMax = 100 # We want to convert the binary value to a number between 0 and 100
  userInput = int(input("Enter a number between 0 and 100: "))

  outputNumber = (binaryMax / 100) * userInput

  print(outputNumber)
