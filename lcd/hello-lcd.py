from lcd1602 import LCD
from time import sleep

lcd = LCD()

while True:
  name = input('What is your name? ')

  lcd.clear()
  greeting1 = f'Hello, {name}!'
  greeting2 = 'Welcome to my Pi'

  lcd.write(0, 0, greeting1)
  lcd.write(0, 1, greeting2)