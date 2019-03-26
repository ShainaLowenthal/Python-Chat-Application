import socket  #the library that allows for chat applications
import sys #Syetem-specific parameters and functions: this module provides access to variables used by the interpreter
import time #Time access and conversions: this module is used for time-relate functions

#initilize the server
s = socket.socket()
host = socket.gethostbyname("") #the host server is initialized to 0.0.0.0 and any client that knows this can access our chat if they run the client file
print("server will start on host: ", host) #lets the user know we are good to go


port = 8080 #can be any number

s.bind((host,port)) 
print("") 
print("Server done binding to host and port successfully!!!")
print("")
print("Server is waiting for incoming connections....")
print("")
s.listen(1) #wait for clients to join server-can be any number of clients and not only one
connection,address = s.accept() #connection is assigned to the socket itself and address is assigned to the IP address of the client

print(address, "has connected to the server and is now online. Let's get this party started!")#lets us know when clients have arrived
print("")



while 1: #puts this in a continuous loop
    message = input(str(">>"))
    message = message.encode() #changes it to bites
    connection.send(message)
    print("message has been sent...")
    print("")
    incoming_message = connection.recv(1024)
    
#now we need to decode it bc it was encoded before
    incoming_message = incoming_message.decode()
    print("Client: ", incoming_message)
    print("")


