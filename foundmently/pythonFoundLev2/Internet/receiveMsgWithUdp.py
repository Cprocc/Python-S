from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)
#绑定地址可以不用指定
#因为可以有两个ip地址，如果想指定其中一个的话可以指定
bindAddress = ('',7788)
udpSocket.bind(bindAddress)


sendAddress = ('192.168.56.1',7789)
# sendData = input("input your send msg:")
# udpSocket.sendto(sendData.encode("gb2312"),sendAddress)
# 1024表示最多收1024字节

while True:
    receiveData = udpSocket.recvfrom(1024)
    content,deInfo = receiveData
    udpSocket.sendto(receiveData[0],receiveData[1])
    if content.decode('utf-8')=="exit":
        print("Client close the content")
        break
    else:
        print("port is",deInfo,"text is",content.decode('gb2312'))


udpSocket.close()
