import time
from socket import *

def comunicacion_tcp_3(puerto):
    HOST = ''
    PORT = puerto
    BUFSIZ = 16
    ADDR = (HOST, PORT)
    data_1=""

    tcpSerSock = socket(AF_INET, SOCK_STREAM)#Inicialización
    tcpSerSock.bind(ADDR)
    tcpSerSock.settimeout(0.2)

    try:
        tcpSerSock.listen()# Puerto de escucha

        tcpCliSock, addr = tcpSerSock.accept()
        data_1 = tcpCliSock.recv(BUFSIZ).decode()
        mensaje="ok"
        tcpCliSock.send(mensaje.encode())



    except:
        pass
    return data_1
