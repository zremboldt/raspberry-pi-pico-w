from machine import Pin, I2C
from ssd1306 import SSD1306_I2C # type: ignore
import socket
import network
import secrets
import json
from time import sleep

# LED setup
ledRed = Pin(14, Pin.OUT)
ledGreen = Pin(15, Pin.OUT)

#---------------------------------
### Display setup
#---------------------------------

# Initialize the I2C bus (for the OLED display)
i2cBus = I2C(id=0, sda=Pin(4), scl=Pin(5), freq=400000) # id is 0 because we are using the I2C0 bus. If we were using I2C1, we would use id=1

# Initialize the display
display = SSD1306_I2C(128, 64, i2cBus) # 128x64 display and we want to talk to it over the I2C bus

def formatAndPrintMessage(message):
  display.fill(0)
  messageChunks = [message[i:i+16] for i in range(0, len(message), 16)]

  for index, chunk in enumerate(messageChunks):
    chunk = chunk.lstrip() # trim whitespace from beginning of chunk
    display.text(chunk, 0, index * 14)

  display.show()

#---------------------------------
# WiFi Setup
#---------------------------------

wifi = network.WLAN(network.STA_IF)
wifi.active(True)
wifi.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore

while not wifi.isconnected():
  print("Connecting...")
  formatAndPrintMessage("Connecting...")
  sleep(1)

serverIp = wifi.ifconfig()[0]
serverPort = 2222
bufferSize = 1024 # defines how many bytes of data we're willing to receive at once

#---------------------------------
# Server setup
#---------------------------------

# Create TCP server instead of UDP
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((serverIp, serverPort))
server.listen(5)

print("Connected to", secrets.wifiName) # type: ignore
print("Server IP address:", serverIp)
print("Server is now listening for incoming messages...")

formatAndPrintMessage("Listening...")

# At this point, our server is running and listening for incoming requests.

def serverCleanup():
  try:
    server.close()
    wifi.disconnect()
    display.fill(0)
    display.show()
  except:
    pass

def handle_request(client):
  try:
    # Receive the full HTTP request
    request = client.recv(bufferSize).decode('utf-8')
    
    # Handle preflight CORS request
    if 'OPTIONS' in request:
      response = 'HTTP/1.1 200 OK\r\n'
      response += 'Access-Control-Allow-Origin: *\r\n'
      response += 'Access-Control-Allow-Methods: POST, OPTIONS\r\n'
      response += 'Access-Control-Allow-Headers: Content-Type\r\n'
      response += '\r\n'
      client.send(response)
      return
    
    # Handle POST request
    if 'POST' in request:
      # Extract the JSON body
      body_start = request.find('\r\n\r\n') + 4
      body = request.split('\r\n\r\n', 1)[1]
        
      try:
        data = json.loads(body)
        message = data.get('message', '')
        print(f"Message received: {message}")
        
        # Send HTTP response
        response = 'HTTP/1.1 200 OK\r\n'
        response += 'Access-Control-Allow-Origin: *\r\n'
        response += 'Content-Type: text/plain\r\n'
        response += '\r\n'
        response += f"200: OK"
        client.send(response)

        return message
      except ValueError:
        # Invalid JSON
        response = 'HTTP/1.1 400 Bad Request\r\n\r\n'
        client.send(response)
    else:
      # Not a POST request
      response = 'HTTP/1.1 405 Method Not Allowed\r\n\r\n'
      client.send(response)
          
  except Exception as e:
    print(f"Error: {e}")
    response = 'HTTP/1.1 500 Internal Server Error\r\n\r\n'
    client.send(response)
  finally:
    client.close()

try:
  while True:
      try:
        client, addr = server.accept()
        print(f"Connection from {addr[0]}")
        message = handle_request(client)

        print(f"Message: {message}")

        if message == "quit":
          formatAndPrintMessage("Shutting down    server...")
          sleep(1)
          serverCleanup()
        elif message == "green":
          if ledGreen.value() == 0:
            ledGreen.on()
          else:
            ledGreen.off()
        elif message == "red":
          if ledRed.value() == 0:
            ledRed.on()
          else:
            ledRed.off()
        else:
          formatAndPrintMessage(message)

      except Exception as e:
        print(f"Server error: {e}")

except KeyboardInterrupt:
  print("Shutting down server...")
  formatAndPrintMessage("Shutting down    server...")
  sleep(1)
  serverCleanup()
finally:
  serverCleanup()

