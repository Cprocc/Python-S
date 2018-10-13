# tcp:Transmission Control Protocol
from socket import *

tcpSerSocket = socket(AF_INET,SOCK_STREAM)
serAddress = ('',7788)
tcpSerSocket.bind(serAddress)
tcpSerSocket.listen(5)  #更改为监听方,5已建立和未建立的队列总长度

while True:
    newClientSocket, tcpClientAddress = tcpSerSocket.accept() #标记一个client,等待client连接

    while True:
        receiveData = newClientSocket.recv(1024) #recvfrom ,recv

        if len(receiveData) > 0:
            print("receiveData is:",receiveData.decode('utf-8'))
        else:
            break

        sendData = input('reply:')
        newClientSocket.send(sendData.encode('utf-8')) #send，sendto

    newClientSocket.close()


tcpSerSocket.close()


