import socket
import threading
import os

def clientthread(conn):
    conn.send("You are connected to the server! Type your message".encode())  # Encode the string
    while True:
        message = conn.recv(2048)
        if not message:
            break
        broadcast(message, conn)
    conn.close()

def broadcast(message, connection):
    for client in clients:
        if client != connection:
            try:
                client.send(message)
            except:
                client.close()
                clients.remove(client)

HOST = '127.16.10.1'
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(10)

print("Chat server started on port " + str(PORT))

clients = []

while True:
    conn, addr = server.accept()
    clients.append(conn)
    print("Connected with " + addr[0] + ":" + str(addr[1]))
    threading.Thread(target=clientthread, args=(conn,)).start()
