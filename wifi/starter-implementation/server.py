import socket
import network
import secrets
from time import sleep

wifi = network.WLAN(network.STA_IF)
wifi.active(True)

wifi.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore

while not wifi.isconnected():
  print("Connecting...")
  sleep(1)

print("Connected to", secrets.wifiName) # type: ignore

serverIp = wifi.ifconfig()[0]
print("Server IP address:", serverIp)
print("Server is now listening for incoming messages...")

serverPort = 2222
bufferSize = 1024 # defines how many bytes of data we're willing to receive at once
udpServer = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # This creates our socket object that uses the UDP protocol
udpServer.bind((serverIp, serverPort)) # This binds our socket to the IP address and port number we defined earlier

# At this point, our server is running and listening for incoming requests. We can now receive data sent to our server using the recvfrom method.

while True:
  message, address = udpServer.recvfrom(bufferSize) # This receives the message sent to our server and the address of the client that sent the message. These are stored in the message and address variables.
  decodedMessage = message.decode("utf-8") # This decodes the message from bytes to a string
  print(f"Message from client {address[0]}: {decodedMessage}")

  # Now that we got the message from the client, we can send a response saying that we received it.

  dataString = f"Message received! You sent: {decodedMessage}"
  dataStringEncoded = dataString.encode("utf-8")
  udpServer.sendto(dataStringEncoded, address) # This sends a response to the client that sent the message
