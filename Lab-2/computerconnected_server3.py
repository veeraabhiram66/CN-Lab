import socket

s=socket.socket()

port = 2522

s.bind(('',port))
print("Socket is binded to %s",port)
s.listen(5)
print("Socket is listening")

while True :
    c,addr = s.accept()
    print("Got connection from ",addr)
    c.send("connected to varun computer" .encode())
    c.close()
    break
