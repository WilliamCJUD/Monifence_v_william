import time
from socket import *

HOST = ''
PORT = 9000
BUFSIZ = 16
ADDR = (HOST, PORT)

def comunicacion_tcp():
    data=""

    tcpSerSock = socket(AF_INET, SOCK_STREAM)#Inicialización
    tcpSerSock.bind(ADDR)
    tcpSerSock.settimeout(0.3)

    try:
        tcpSerSock.listen()# Puerto de escucha
        tcpCliSock, addr = tcpSerSock.accept()
        #print('connected from:{}'.format(addr))
        #tcpCliSock.open()
        data = tcpCliSock.recv(BUFSIZ).decode()
        ip=addr[0]
        #print(ip)
        mensaje="ok"
        tcpCliSock.send(mensaje.encode())
        tcpCliSock.close()
    except:
        pass
    return data
# while True:
#     mensaje= comunicacion_tcp()
#     if len(mensaje)>0:
#         print(mensaje)
