#Roll.No:CS21B2026
#Name:P.Veera Abhiram
import socket
import sys
import os

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print('starting up on {} port {}'.format(*server_address))
sock.bind(server_address)
sock.listen(5)

while True:
    print('waiting for a connection')
    connection, client_address = sock.accept()
    print('connection from', client_address)

    def receive_file(filename): 
        data = connection.recv(1024).decode()
        file = open(filename, 'w')
        file.write(data)
        message = 'File data received successfully'
        connection.send(message.encode())
        file.close()

    def send_file(filename):
        if os.path.isfile(filename):
            data = read_file(filename)
            connection.send(data.encode())
            message = 'File data sent successfully'
            connection.send(message.encode())
        else:
            message = 'File does not exist'
            connection.send(message.encode())

    def read_file(filename):
        file = open(filename, 'r')
        data = file.read()
        return data
    
    while True:
        print('1. Receive file from client')
        print('2. Send file to client')
        print('3. Exit')

        choice = int(input('Enter your choice: '))
        match choice:
            case 1:
                filename = input('Enter filename: ')
                receive_file(filename)
            case 2:
                filename = input('Enter filename: ')
                send_file(filename)
            case 3:
                break
            case _:
                print('Invalid choice')

    connection.close()
    sys.exit() 

sock.close()
sys.exit()
