from machine import Pin, PWM

ledRed = PWM(Pin(13))
ledGreen = PWM(Pin(12))
ledBlue = PWM(Pin(11))

ledRed.freq(1000)
ledGreen.freq(1000)
ledBlue.freq(1000)

while True:
  binaryMax = 65535
  humanReadableMax = 100
  getBinaryValue = lambda value: round((binaryMax / humanReadableMax) * value)

  def setColor(red, green, blue):
    ledRed.duty_u16(getBinaryValue(red))
    ledGreen.duty_u16(getBinaryValue(green))
    ledBlue.duty_u16(getBinaryValue(blue))

  userInput = input("Choose your color: ")

  if userInput == "red":
    setColor(100, 0, 0)
  elif userInput == "green":
    setColor(0, 100, 0)
  elif userInput == "blue":
    setColor(0, 0, 100)
  elif userInput == "cyan":
    setColor(0, 100, 100)
  elif userInput == "magenta":
    setColor(100, 0, 100)
  elif userInput == "yellow":
    setColor(100, 30, 0)
  elif userInput == "orange":
    setColor(100, 10, 0)
  elif userInput == "white":
    setColor(100, 100, 100)
  else:
    print("Invalid color")