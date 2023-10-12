'''
Bryce Thorpe
Written in University of Arizona CYBV 473 - Violent Python
Scripting Assignment 10 - Create TCP Server
2/28/23

Simple Server to receive data from and echo back to client
Echos back message in plaintext + MD5 Hex Digest
NOTE: SERVER MUST BE STARTED AS ADMIN

In this example a connection is made between a client
and simple server running on the same machine over a 
pre-defined and agreed upon port.

This server application will wait for a connection request
over a pre-defined port.

Once a connection is established the server will receive data sent 
over the port, display the contents of the recevied data, generate an
MD5 hash hex digest of the message content, and echo it back to the 
client. 

'''

import socket       # import Python Standard Socket Library
import sys
import hashlib

print("Server Starting up\n")
    
try: 
    
    serverSocket = socket.socket()      # Create Socket for listening
    
    localHost = socket.gethostname()    # Get my local host address
    
    localPort = 5555                    # Specify a local Port 
                                        # to accept connections on
    
    serverSocket.bind((localHost, localPort))  # Bind mySocket to localHost
    
    serverSocket.listen(1)              # Listen for connections

    print('\nWaiting for Connection Request')    
    
    ''' Wait for a connection request
        Note this is a synchronous Call meaning the program will halt until
        a connection is received.  Once a connection is received
        we will accept the connection and obtain the 
        ipAddress of the connecting computer
    '''
    
    conn, client = serverSocket.accept()
    
    
    print("Connection Received from Client: ", conn, client)
    
    while True:
        buffer = conn.recv(2048)  # Wait for Data
        print(buffer)  
        
        if b'exit' in buffer.lower():
            print("Server Terminated by User") # Exits when 'exit' is recieved
            break
        
        if b'continue' in buffer.lower():
            print('Messages Incoming...')
            continue
        else: 
            md5Obj = hashlib.md5()
            md5Obj.update(buffer)
            digest = md5Obj.hexdigest()
            digestBytes = bytes(str(digest).encode("utf-8"))   # Encodes HexDigest of message into bytes string
    
            response= b'Got your message: ' +buffer+b' MSG-Hash: '+digestBytes
            print(response)
            conn.sendall(response)   
    
except Exception as err:
    sys.exit(str(err))

