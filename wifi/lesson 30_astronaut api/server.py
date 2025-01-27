import network
from time import sleep
import urequests # This library allows us to make requests to API's over the internet
import secrets

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore

while not wifi.isconnected():
  print("Connecting...")
  sleep(1)

print("Connected!")
print()

try:
  response = urequests.get("http://api.open-notify.org/astros.json").json()

  print(f"There are currently {response['number']} people in space:")

  for person in response["people"]:
    print(f"- {person['name']} is aboard the {person['craft']}.")

except Exception as e:
  print("Error:", e)