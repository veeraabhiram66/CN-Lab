#Single Server and Multiple Client Communication - Python Socket Programming
#Write a Server program with threads, where each thread can handle a single client.
#Ensure server get connected to multiple clients.
#All the client messages to be displayed in server.
#Provide a mechanism to disconnect the client.


#Implement with python socket programming.
#1) Demonstrate with local loop IP
#2) Connect with multiple client with different IPs
#3) Modify the program where server can send messages to specific client.

import socket
import threading
import sys

class Server:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connections = []
    def __init__(self):
        self.sock.bind(('', 10000))
        self.sock.listen(1)
        print("Server Running...")
    def handler(self, c, a):
        while True:
            data = c.recv(1024)
            for connection in self.connections:
                connection.send(data)
            if not data:
                print(str(a[0]) + ':' + str(a[1]), "disconnected")
                self.connections.remove(c)
                c.close()
                break
    def run(self):
        while True:
            c, a = self.sock.accept()
            cThread = threading.Thread(target=self.handler, args=(c, a))
            cThread.daemon = True
            cThread.start()
            self.connections.append(c)
            print(str(a[0]) + ':' + str(a[1]), "connected")

class Client:
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def sendMsg(self):
        while True:
            self.sock.send(bytes(input(""), 'utf-8'))
    def __init__(self, address):
        self.sock.connect((address, 10000))
        iThread = threading.Thread(target=self.sendMsg)
        iThread.daemon = True
        iThread.start()
        while True:
            data = self.sock.recv(1024)
            if not data:
                break
            print(str(data, 'utf-8'))

if(len(sys.argv) > 1):
    client = Client(sys.argv[1])
else:
    server = Server()
    server.run()