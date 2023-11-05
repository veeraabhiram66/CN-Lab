import socket

s = socket.socket()
port = 35352
s.connect(('172.20.10.3',port))
print(s.recv(1024).decode())
s.close()