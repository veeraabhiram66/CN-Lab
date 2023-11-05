#Roll.No:CS21B2026
#Name:P.Veera Abhiram
import socket
import readline
import threading
import time

IP = socket.gethostbyname(socket.gethostname())
PORT = 5567
ADDR = (IP, PORT)
SIZE = 1024
DISCONNECT_MESSAGE = "!DISCONNECT"

list_of_clients = []

curr_msg = ""

def print_msg(msg):                    #function to print message
    input_buffer = readline.get_line_buffer()
    print(f"\r{msg}\n{curr_msg}{input_buffer}",end="",flush=True)

def input_msg(input_str):              #function to take input
    global curr_msg
    curr_msg = input_str
    output = input(f"\r{input_str}")
    return output

def send_msg(address,msg):                #function to send message
    for client in list_of_clients:
        if client["addr"] == address:
            client["conn"].send(msg.encode()) 
            break
        
def send_file(conn, addr):                   #function to send file
    print_msg(f"[NEW CONNECTION] {addr} connected.")
    for client in list_of_clients:        
        if client["addr"] != addr:
            conn.send(f"l:({client['addr'][0]} {client['addr'][1]}) connected to server".encode())
    for client in list_of_clients:
        if client["addr"] != addr:
            client["conn"].send(f"l:({addr[0]} {addr[1]}) connected to server".encode())

    connected = True
    while connected:
        ip_port = conn.recv(SIZE).decode()
        if not ip_port:
            continue

        if ip_port == DISCONNECT_MESSAGE:
            connected = False
            for client in list_of_clients:
                if client["addr"] != addr:
                    client["conn"].send(f"l:({addr[0]} {addr[1]}) disconnected from server".encode())
            for client in list_of_clients:
                if client["addr"] == addr:
                    list_of_clients.remove(client)
                    break
            else:
                print_msg(f"[ERROR]  {addr}")  
            print_msg(f"\r[DISCONNECT CONNECTION] {addr} disconnected.")
            print_msg(f"[ACTIVE CONNECTIONS] {threading.active_count() - 2}")
            break
        
        address =(ip_port.split(' ')[0], int(ip_port.split(' ')[1]))
        for client in list_of_clients:
            if client["addr"] == address:
                break
        else:
            conn.send(f"e: {address} not found.".encode())
            continue
        
        file_name = conn.recv(SIZE).decode()
        send_msg(address,file_name)

        for client in list_of_clients:
            if client["addr"] == address:
                send_conn = client["conn"]
        data = conn.recv(SIZE)
        while data != b"EOF":
            send_conn.send(data)
            data = conn.recv(SIZE)
        time.sleep(0.1)
        send_conn.send(b"EOF")
        conn.send("a:[SENT] File sent.".encode())
        ack = send_conn.recv(SIZE).decode()
        conn.send(f"{ack} by {address}".encode())
    conn.close()

if __name__=="__main__":
    print_msg("[STARTING] Server is starting...")
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(ADDR)
    server.listen()
    print_msg(f"[LISTENING] Server is listening on {IP}:{PORT}")

    while True:
        conn, addr = server.accept()
        list_of_clients.append({"addr":addr, "conn":conn})
        thread = threading.Thread(target=send_file, args=(conn,addr))
        thread.start()
        print_msg(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")
