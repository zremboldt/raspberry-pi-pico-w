from machine import Pin, PWM
from time import sleep

motor_A = PWM(Pin(14))  # Connected to FI on TA6586
motor_B = PWM(Pin(15))  # Connected to BI on TA6586

motor_A.freq(1000)  # 1 kHz PWM frequency
motor_B.freq(1000)

def convertPercentageToDutyCycle(percentage):
  if percentage < 0 or percentage > 100:
    raise ValueError("Percentage must be between 0 and 100.")
  
  # Map 0-100% to 15000-65535
  duty_cycle = int((percentage / 100) * (65535 - 15000) + 15000)
  return duty_cycle

def motor_forward(power=50):
    motor_A.duty_u16(convertPercentageToDutyCycle(power))
    motor_B.duty_u16(0)

def motor_backward(power=50):
    motor_A.duty_u16(0)
    motor_B.duty_u16(convertPercentageToDutyCycle(power))

def motor_stop():
    motor_A.duty_u16(0)
    motor_B.duty_u16(0)

# Test sequence
motor_forward(10)
sleep(0.5)
motor_forward(50)
sleep(0.5)
motor_forward(100)
sleep(1)
motor_stop()
sleep(0.5)
motor_backward(10)
sleep(0.5)
motor_backward(50)
sleep(0.5)
motor_backward(100)
sleep(1)
motor_stop()
