
import socket
import sys
import os
from server import file

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('connecting to {} port {}'.format(*server_address))
sock.connect(server_address)

def read_file(filename):
    file = open(filename, 'r')
    data = file.read()
    return data

def send_file(filename):
    data = read_file(filename)
    sock.send(filename.encode())
    message = sock.recv(1024).decode()
    print(message)
    sock.send(data.encode())
    message = sock.recv(1024).decode()
    print(message)
    file.close()

def receive_file(filename):
    sock.send(filename.encode())
    message = sock.recv(1024).decode()
    print(message)
    data = sock.recv(1024).decode()
    file = open(filename, 'w')
    file.write(data)
    message = 'File data received successfully'
    sock.send(message.encode())
    file.close()

while True:
    print('1. Send file to server')
    print('2. Receive file from server')
    print('3. Exit')
    opt = int(input('Enter your option: '))
    match(opt):
        case 1:
            filename = input('Enter the filename: ')
            send_file(filename)
        case 2:
            filename = input('Enter the filename: ')
            receive_file(filename)
        case 3:
            sock.close()
            sys.exit()
        case _:
            print('Invalid option')
            sock.close()
            sys.exit()

sock.close()
sys.exit()
