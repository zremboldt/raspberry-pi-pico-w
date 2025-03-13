from machine import Pin, PWM
from time import sleep

print("Lego motor test script")
# Define motor control pins
motor_A = PWM(Pin(14))  # Connected to BI on TA6586
motor_B = PWM(Pin(15))  # Connected to FI on TA6586

# Set PWM frequency
motor_A.freq(1000)  # 1 kHz PWM frequency
motor_B.freq(1000)

def motor_forward(speed=512):
    print("Run motor forward at a given speed (0-1023).")
    motor_A.duty_u16(speed)  # Set duty cycle (0-65535)
    motor_B.duty_u16(0)      # Turn off other direction

def motor_backward(speed=512):
    print("Run motor backward at a given speed (0-1023).")
    motor_A.duty_u16(0)
    motor_B.duty_u16(speed)

def motor_stop():
    print("Stop the motor.")
    motor_A.duty_u16(0)
    motor_B.duty_u16(0)

# Test sequence
motor_forward(40000)  # Forward at ~60% power
sleep(1)
motor_backward(40000)  # Backward at ~60% power
sleep(1)
motor_stop()