import socket
import threading
import sys

SERVER_ADDRESS = ('localhost', 8001)

clients_name=[]
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(SERVER_ADDRESS)

if len(clients_name)< 10:
    client_name = input("Enter client name: ")
    client_socket.send(client_name.encode())
    clients_name.append(clients_name)

    print("Connected to the server.")

else:
    print("Max clients")

client_socket.close()