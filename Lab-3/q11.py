#1) Demonstrate with local loop IP

import socket
import threading

def client_handler(client_socket, client_address):
    print("Accepted connection from: ", client_address)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received data from client: ", data.decode())
        client_socket.send(data)
    client_socket.close()
    print("Client disconnected: ", client_address)

def main():
    host = '172.17.0.239'
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server listening on port: ", port)
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
        client_thread.start()

if __name__ == '__main__':
    main()

'''
#2) Connect with multiple client with different IPs

import socket
import threading

def client_handler(client_socket, client_address):
    print("Accepted connection from: ", client_address)
    while True:
        data = client_socket.recv(1024)
        if not data:
            break
        print("Received data from client: ", data.decode())
        client_socket.send(data)
    client_socket.close()
    print("Client disconnected: ", client_address)

def main():
    host = '
    port = 5000
    server_socket = socket.socket()
    server_socket.bind((host, port))
    server_socket.listen(5)
    print("Server listening on port: ", port)
    while True:
        client_socket, client_address = server_socket.accept()
        client_thread = threading.Thread(target=client_handler, args=(client_socket, client_address))
        client_thread.start()
        
if __name__ == '__main__':
    main()

'''