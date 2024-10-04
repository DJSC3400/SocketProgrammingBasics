# -*- coding: utf-8 -*-
"""
Created on Fri Oct  4 10:07:13 2024

@author: School
"""

import socket
import sys

HOST = ''
PORT = 9999

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print ('Socket created!')

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print('bind failed. Error code :'+str(msg[0])+'Message'+ msg[1])
    #print(f'bind failed. Error code : {str(msg[0])} Message {msg[1]}')
    sys.exit()
    
print ('Socket bind complete')
s.listen(10)
print ('Socket is now listening...')

while True:
    try:
        innerSocket, address = s.accept()
        connect = 'Connected with ' +address[0]+':'+str(address[1])
        print (connect)
        innerSocket.send(connect.encode('utf-8'))
        
        response = ""
        message = ""
        
        
        while ((response != "goodbye") and (message != "goodbye")):
            response = innerSocket.recv(500).decode('utf-8')
            print (response)
            if (response == "goodbye"): break
            message = input(" :")
            bitMessage = message.encode('utf-8')
            innerSocket.send(bitMessage)
        
        disconnect = 'Disconnected from ' +address[0]+':'+str(address[1])
        print("")
        print (disconnect)
        innerSocket.send(disconnect.encode('utf-8'))
        innerSocket.close()
    
    except socket.error as msg:
        print('accept failed. Error code :'+str(msg[0])+'Message'+ msg[1])
        innerSocket.close()

s.close()
