from machine import PWM, Pin
from time import sleep

servo = PWM(Pin(15))
servo.freq(50) # 50Hz

try:
  def degToDuty(desiredDegrees):
    deg0 = 1570 # 0 degrees from duty cycle
    deg180 = 7900 # 180 degrees from duty cycle
    return int((((deg180 - deg0) / 180) * desiredDegrees) + deg0)

  while True:
    servo.duty_u16(degToDuty(0))
    sleep(1)
    servo.duty_u16(degToDuty(45))
    sleep(1)
    servo.duty_u16(degToDuty(90))
    sleep(1)
    servo.duty_u16(degToDuty(135))
    sleep(1)
    servo.duty_u16(degToDuty(180))
    sleep(1)

except KeyboardInterrupt:
  servo.deinit()