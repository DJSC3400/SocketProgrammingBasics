# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:11:41 2024

@author: School
"""

import socket

HOST = '127.0.0.1' # localhost 10.220.53.68
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((HOST,PORT))

response = s.recv(500).decode('utf-8')
print (response)

response = ""
message = ""

while ((response != "goodbye") and (message != "goodbye")):
    message = input(" :")
    bitMessage = message.encode('utf-8') #bytes("{}".format(message), 'utf-8') 
    s.send(bitMessage)
    if (response == "goodbye"): break
    response = s.recv(500).decode('utf-8')
    print (response)

print("")
response = s.recv(500).decode('utf-8')
print (response)
s.close()
