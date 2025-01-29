from machine import Pin, PWM, ADC
from time import sleep

def degToDuty(desiredDegrees):
  deg0 = 1570 # duty cycle resulting in 0 degrees
  deg180 = 7900 # duty cycle resulting in 180 degrees
  return int((((deg180 - deg0) / 180) * desiredDegrees) + deg0)

servo = PWM(Pin(15))
servo.freq(50) # 50Hz
servo.duty_u16(degToDuty(0))

potPin = 28 # Pin for the potentiometer
potentiometer = ADC(potPin) # Create an Analog to Digital Conversion object

potMax = 65535 # 65535 is the maximum value I get from my potentiometer
potMin = 272 # 272 is the minimum value I get from my potentiometer

try:
  while True:
    potentiometerValue = potentiometer.read_u16() # Read the potentiometer value. u16 gives us a 16 bit binary number.

    # Convert the potentiometer value to a number between 0 and 180 degrees
    potToDegrees = max(0, round((180 - 0) * ((potentiometerValue - potMin) / (potMax - potMin))))

    servo.duty_u16(degToDuty(potToDegrees))

    print(f"Potentiometer Value: {potentiometerValue} ... potToDegrees: {potToDegrees}")
    sleep(0.02)

except KeyboardInterrupt:
  servo.deinit()