# udp:User Datagram Protocol
from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
#绑定地址可以不用指定
#因为可以有两个ip地址，如果想指定其中一个的话可以指定
bindAddress = ('',7789)
sendAddress = ('192.168.56.1',7788)

udpSocket.bind(bindAddress)

while True:
    sendData = input("input your send msg:")
    if sendData == "exit":
        udpSocket.sendto("exit".encode("utf-8"),sendAddress)
        break
    else:
        udpSocket.sendto(sendData.encode("gb2312"), sendAddress)
    receiveData = udpSocket.recvfrom(1024)
    content,deInfo = receiveData
    print("port is",deInfo,"text is",content.decode('gb2312'))
# 1024表示最多收1024字节
# receiveData = udpSocket.recvfrom(1024)
# content,deInfo = receiveData
# print("port is",deInfo,"text is",content.decode('gb2312'))
udpSocket.close()