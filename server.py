import socket
from threading import Thread

IP_ADDRESS='127.0.0.1'
PORT= 8050
SERVER= None
BUFFER_SIZE= 4096
Clients= {}

def setup ():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')

    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket. socket (socket .AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER. listen (100)

    print ("\t\t\t\tSERVER IS WAITING FOR INCOMMING CONNECTIONS...")
    print("\n")

def acceptconnections():
    global SERVER
    global Clients

    while True:
        client, addr= SERVER.accept()
        client_name= client.recv(4096).decode().lower()
        Clients[client_name] = {
                'client'       : client,
                'address'      : addr,
                'connected_with': "",
                'file_name'    : "",
                'file_size'   : 4096
        }
    print(f'connection established with {client_name} : {addr}')

    thread= Thread(target= handleClient, args= (client,client_name,))
    thread.start()

def setup ():
    print('\n\t\t\t\t\t\tIP MESSENGER\n')


    # Getting global values
    global PORT
    global IP_ADDRESS
    global SERVER

    SERVER = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    SERVER.bind((IP_ADDRESS, PORT))

    SERVER. Listen (100)

    print('\t\t\t\tSERVER IS WAITING FOR INCONMING CONNECTIONS...')
    print ("\n")


    acceptconnections ()

setup_thread = Thread (target=setup) #receiving multiple messages
setup_thread.start()