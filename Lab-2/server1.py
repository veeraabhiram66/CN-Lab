import socket

s=socket.socket()

port = 12345

s.bind(('',port))
print("Socket is binded to %s",port)
s.listen(5)
print("Socket is listening")

while True :
    c,addr = s.accept()
    print("Got connection from ",addr)
    c.send("Thank you for Connecting -- HP-Pavilion" .encode())
    c.close()
    break
