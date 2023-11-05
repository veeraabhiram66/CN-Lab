#Roll No: CS21B2026
#Name: P.Veera Abhiram
import socket
import threading

IP= '172.17.1.61'
PORT= 12345
ADDR= (IP, PORT)
SIZE= 1024
FORMAT= "utf-8"
DISCONNECT_MESSAGE= "!DISCONNECT"

def main():
    client= socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(ADDR)
    print(f"[CONNECTED] Client Connected to {IP}:{PORT}")

    connected= True
    while connected:
        msg=input("[MESSAGE] Enter a message: ")
        client.send(msg.encode(FORMAT))
        if msg== DISCONNECT_MESSAGE:
            connected= False
        else:
            msg= client.recv(SIZE).decode(FORMAT)
            print(f"[SERVER] {msg}")

if __name__== "__main__":
    main()
