# TCP Client and Server - Python Scripts

This repository contains two Python scripts for creating a simple TCP client and server to transfer data in the clear with echo.

## Server

### Description

The `TCPServer.py` script is a simple server that waits for a connection request over a pre-defined port. Once a connection is established, the server receives data sent over the port, displays the contents of the received data, generates an MD5 hash hex digest of the message content, and echoes it back to the client.

### Usage

1. Run the server script as sudo using Python3:

   ```bash
   sudo python3 TCPServer.py
   ```
   
3. Wait for the incoming client request. 

## Client

### Description

The `TCPClient.py` script demonstrates a client application that connects to a server running on the same host over a pre-defined and agreed-upon port. The client transfers a list of text messages to the server, one by one. The server displays the contents of the message and echoes back the message along with its MD5 hash hex digest.

### Usage

1. Run the client script as sudo using Python3:

     ```bash
     sudo python TCPClient.py
     ```
     
2. Type `continue` to continue or `exit` to exit the program. Wait for the server to return the messages back along with the hashes.
