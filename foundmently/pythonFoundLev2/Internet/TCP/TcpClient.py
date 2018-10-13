from socket import *

tcpClientSocket = socket(AF_INET,SOCK_STREAM)

serAddress = ('192.168.56.1',7788)
tcpClientSocket.connect(serAddress)

while True:
    sendData = input('send to service:')
    tcpClientSocket.send(sendData.encode('utf-8'))
    receiveData = tcpClientSocket.recv(1024)

    if len(receiveData) > 0:
        print('receive from client:',receiveData.decode('utf-8'))
    else:
        break

tcpClientSocket.close()