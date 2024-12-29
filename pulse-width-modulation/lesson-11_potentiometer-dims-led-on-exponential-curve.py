from machine import Pin, PWM, ADC
from time import sleep

ledPin = 11
analogLedPin = PWM(Pin(ledPin)) # Set the pin as a PWM output
analogLedPin.freq(1000) # Set the frequency of the PWM signal to 1000Hz. This will blink once per millisecond. Play with the value if desired.
analogLedPin.duty_u16(0) # Set the duty cycle of the PWM signal. This is a 16 bit binary number. 0 is off and 65535 is fully on.

potPin = 28 # Pin for the potentiometer
pot = ADC(potPin) # Create an Analog to Digital Conversion object

while True:
  potentiometerValue = pot.read_u16() # Read the potentiometer value. u16 gives us a 16 bit binary number.
  exponentialValue = (16/65535) * potentiometerValue
  brightness = int(2 ** exponentialValue) - 1

  print(f"Potentiometer Value: {potentiometerValue} ...... Exponential Value: {exponentialValue} ...... LED Brightness: {brightness}")

  analogLedPin.duty_u16(brightness)

  sleep(0.1)
