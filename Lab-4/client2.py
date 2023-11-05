import socket
import sys
import threading

def send():
    while True:
        message = input("<client-2> ")
        client.send(message.encode()) 

def receive():
    while True:
        message = client.recv(2048)
        print("<Other> " + message.decode()) 

HOST = '127.16.10.1' 
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

try:
    client.connect((HOST, PORT))
except socket.error as msg:
    print("Connect failed. Error Code: " + str(msg[0]) + " Message: " + msg[1])
    sys.exit()

print("Socket connected")

threading.Thread(target=send).start()
threading.Thread(target=receive).start()

