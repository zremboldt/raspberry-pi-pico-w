After the Pico server is running it will print the ip address to the console.
Now control the Pico by sending commands to the server.

One option would be to use curl along with the given IP address from the command line:
`curl http://222.222.2.222/light-on`
`curl http://222.222.2.222/light-off`

Or you can run the index.html file in this folder and enter the IP address in the field at the top.
Subsequent button presses will send fetch requests to the same server endpoints as mentioned above.
