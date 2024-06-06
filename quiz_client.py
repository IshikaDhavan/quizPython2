import socket
from threading import Thread

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

name = "Write your name: "
ipaddr = "127.0.0.1"
port = 7500

client.connect((ipaddr,port))
print("connected with server")

def recieve():
    while True:
        try:
            message = client.recv(2048).decode('utf-8')
            if message == 'NICKNAME':
                client.send(name.encode('utf-8'))
            else:
                print(message)
        except:
            print("An error occured")
            client.close()
            break

def write():
    while True:
        message = input('')
        client.send(message.encode('utf-8'))

recieve_thread = Thread(target= recieve)
recieve_thread.start()

write_thread = Thread(target= write)
write_thread.start()
