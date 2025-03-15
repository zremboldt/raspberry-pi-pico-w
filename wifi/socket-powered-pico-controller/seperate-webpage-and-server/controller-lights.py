import network
import socket
from time import sleep
import machine
import secrets

led = machine.Pin(16, machine.Pin.OUT)

def move_forward():
    print ("Forward")

def move_backward():
    print ("Backward")
    
def move_stop():
    print ("Stop")
    
def move_left():
    print ("Left")
    
def move_right():
    print ("Right")
    
def light_on():
    print ("On")
    led.on()
    
def light_off():
    print ("Off")
    led.off()
    
def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True)
    wlan.connect(secrets.wifiName, secrets.wifiPassword) # type: ignore
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return ip
    
def open_socket(ip):
    # Open a socket
    address = (ip, 80)
    connection = socket.socket()
    connection.bind(address)
    connection.listen(1)
    return connection

def serve(connection):
    #Start web server
    while True:
        client = connection.accept()[0]
        request = client.recv(1024)
        request_str = str(request)
        
        # Check if this is an OPTIONS request (CORS preflight)
        if "OPTIONS" in request_str:
            response = "HTTP/1.1 200 OK\r\n"
            response += "Access-Control-Allow-Origin: *\r\n"
            response += "Access-Control-Allow-Methods: GET\r\n"
            response += "Access-Control-Allow-Headers: *\r\n"
            response += "\r\n"
            client.send(response)
            client.close()
            continue
            
        try:
            request_path = request_str.split()[1]
        except IndexError:
            request_path = "/"
            
        # Process commands
        response_text = "Command received"
        if request_path == '/forward':
            move_forward()
        elif request_path =='/left':
            move_left()
        elif request_path =='/stop':
            move_stop()
        elif request_path =='/right':
            move_right()
        elif request_path =='/back':
            move_backward()
        elif request_path =='/light-on':
            light_on()
        elif request_path =='/light-off':
            light_off()
        else:
            response_text = "Unknown command"
        
        try:
          # Send response with CORS headers
          response = "HTTP/1.1 200 OK\r\n"
          response += "Content-Type: text/plain\r\n"
          response += "Access-Control-Allow-Origin: *\r\n"
          response += "\r\n"
          response += response_text
          
          client.send(response)
          client.close()
        except Exception as e:
          print(f"Error sending response: {e}")
          client.close()
          continue

try:
    ip = connect()
    connection = open_socket(ip)
    serve(connection)
except KeyboardInterrupt:
    machine.reset()