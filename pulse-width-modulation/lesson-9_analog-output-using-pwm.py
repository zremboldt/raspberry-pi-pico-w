from machine import Pin, PWM
from time import sleep

outPin = 16
analogOut = PWM(Pin(outPin))
analogOut.freq(1000)
analogOut.duty_u16(0)

while True:
  