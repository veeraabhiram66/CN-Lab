import socket
import threading
import sys

PORT = 8000

MAX_CONNECTIONS = 1

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('localhost', PORT))
server_socket.listen(MAX_CONNECTIONS)

print("Server is listening for clients...")

clients = {
    'S0': [],
    'S1': [],
    'S2': [],
    'S3': [],
    'S4': []
}

while True:
    client_socket, client_address = server_socket.accept()
    print(f"Connection established with {client_address}")
    
    client_name = client_socket.recv(1024).decode()
    
    if client_name in clients.keys():
        clients[client_name].append(client_socket)
        
        if client_name == 'S0':
            if len(clients[client_name]) > 1:
                old_client_socket = clients[client_name].pop(0)
                old_client_socket.send("You are disconnected.".encode())
                old_client_socket.close()
        elif client_name == 'S1':
            if len(clients[client_name]) > 1:
                disconnected_socket = clients[client_name].pop(0)
                disconnected_socket.send("You are disconnected.".encode())
                disconnected_socket.close()
        elif client_name == 'S2' or client_name == 'S3':
            if len(clients[client_name]) > 1:
                disconnected_socket = clients[client_name].pop(0)
                disconnected_socket.send("You are disconnected.".encode())
                disconnected_socket.close()
        elif client_name == 'S4':
            if len(clients[client_name]) > 1:
                disconnected_socket = clients[client_name].pop(0)
                disconnected_socket.send("You are disconnected.".encode())
                disconnected_socket.close()
                for server in ['S1', 'S2', 'S3']:
                    for client_socket in clients[server]:
                        client_socket.send("You are disconnected.".encode())
                        client_socket.close()
                    clients[server] = []
    else:
        client_socket.send("Invalid server name.".encode())
        client_socket.close()


