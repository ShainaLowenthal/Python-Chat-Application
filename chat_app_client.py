import socket
import sys
import time

s=socket.socket()
host = input(str("Please enter the host name of the server: "))
port = 8080
#s.bind((host,port)) error occured here so I changed it to connect
s.connect((host,port))
print("Connected to chat server") #otherwise it will be an error



while 1:
    incoming_message = s.recv(1024)
#now we need to decode it bc it was encoded before
    incoming_message = incoming_message.decode()
    print("server: ", incoming_message)
    print("")
    message = input(str(">>"))
    message = message.encode() #changes it to bites
    s.send(message)
    print("message has been sent...")
    print("")
