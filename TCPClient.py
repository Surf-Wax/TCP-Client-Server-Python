'''
Bryce Thorpe
Written in University of Arizona CYBV 473 - Violent Python
Scripting Assignment 11 - Create TCP Client
2/28/23

Simple Client Data Transfer in the clear with echo

In this example a connection is made between a client
and simple server running on the same machine over a 
pre-defined and agreed upon port.

This client application will transfer a list of text messages
to the server, one by one. The server will will simply display the 
contents of the message and echo back the message along with it's MD5 Hash 
hex digest of the contents.

'''

import socket           # Import Python Standard Socket Library
import sys
import time

print("Client Application")
print("Establish a connection to a server")
print("Available on the same host using PORT 5555")

PORT = 5555          # Port Number of Server

msgList = ['Oh there', 'once', 'was a', 'hero named', 'Ragnar the red', 'who came', 'riding to', 'Whiterun', 'from ole',  'Rorikstead']

try:
    # Create a Socket
    clientSocket = socket.socket()
    
    # Get my local host address
    localHost = socket.gethostname()
    
    print("\nAttempt Connection to: ", localHost, PORT)
    
    clientSocket.connect((localHost, PORT))
    
    # Sending message if there was a connection
    print("Socket Connected ...")
    print("Sending Message to Server")
    
    while True:
        exitPrompt = input('Type "exit" to close connection, else, type "continue"')
        msg = exitPrompt
        messageBytes = bytes(str(msg).encode("utf-8"))
        clientSocket.sendall(messageBytes)
        
        if 'exit' in exitPrompt:
            print('Session Terminated')
            sys.exit()
        
        count = 1
        for item in msgList:
            msg = str(str(count)+': '+item)
            count += 1
            messageBytes = bytes(str(msg).encode("utf-8"))
            clientSocket.sendall(messageBytes)
            time.sleep(.01)
            
            buffer = clientSocket.recv(2048)
            print(buffer)
    
    
except Exception as err:
    sys.exit(err)

            
