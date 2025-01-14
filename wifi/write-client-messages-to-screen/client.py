import socket

# You can run this client code from the terminal. From this directory just run: python3 client.py

# This is the IP address of the server but it can change if you restart your router. If you need to find the IP address of your server, you can print the serverIp variable to the console in your server file.
serverIp = "192.168.0.201"
serverPort = 2222
serverAddress = (serverIp, serverPort)
bufferSize = 1024
udpClient = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
  message = input("Enter a message to send to the server: ")
  encodedMessage = message.encode("utf-8")
  udpClient.sendto(encodedMessage, serverAddress)

  # Message sent to server, now we wait for a response

  response, address = udpClient.recvfrom(bufferSize)
  decodedResponse = response.decode("utf-8")
  print(f"Response from server: {decodedResponse}")