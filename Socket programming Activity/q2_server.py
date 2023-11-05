import socket
import threading
import sys

MAX_CONNECTIONS = 5
TOTAL_CONNECTIONS = 10
PORT = 8001

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(MAX_CONNECTIONS)

print("Server is listening for clients...")

clients = []

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    if len(clients) < MAX_CONNECTIONS:
        clients.append(client_socket)
        print(f"Client {len(clients)} connected to Server-S.")
    else:
        if( len(clients) < TOTAL_CONNECTIONS):
            print(f"Transferring client {len(clients) + 1} to Server-Sr.")
            
            clients.append(client_socket)
            
        else:
            print("Max clients reached")
            sys.exit()