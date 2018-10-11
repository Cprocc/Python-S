# down files //client
# 顺序
## 首先请求，Tftp端口号为69.发送下载请求。69只接受下载请求，之后的数据由随机端口发
## Tftp 服务器回复方式是以数据片的方式给到。
## 确认重传，发送下一个时上一个数据包必须得到确认
## 用操作码标识文件时不存在，还是文件内容。收到的是数据内容则不需要确认
## 操作码1:读请求，即下载 2:写请求，即上传 3:数据包4：ack5：Error
## 何时代表传输完毕：当收到的数据长度小于516 2+2+512 操作码加块编号加数据
from socket import *
import struct
import sys

if len(sys.argv) != 2:
    print('-'*30)
    print("tips:")
    print("python xxx.py 192.168.1.1")
    print('-'*30)
    exit()
else:
    ip = sys.argv[1]


udpSocket = socket(AF_INET,SOCK_DGRAM)
udpSocket.bind(('',5555))
#H占2字节 8s八个char，b一个字节
cmd_buf = struct.pack("!H8sb5sb",1,bytes(("test.jpg").encode('utf-8')),0,bytes(('octet').encode('utf-8')),0)
udpSocket.sendto(cmd_buf,("192.168.56.1",69))

p_num = 0
receiveFile = ''

while True:
    receiveData,receiveAddress = udpSocket.recvfrom(1024)
    receiveDataLen = len(receiveData)
    cmdTuple = struct.unpack("!HH", receiveData[:4])
    cmd = cmdTuple[0]
    currentPackNum = cmdTuple[1]

    if cmd == 3:
        if currentPackNum == 1:
            receiveFile = open("test.jpg",'a')

        if p_num + 1 == currentPackNum:
            receiveFile.write(receiveData[4:])
            p_num += 1
            print("%d次收到的数据"%(p_num))
            ackBuf = struct.pack("!HH",4,p_num)
            udpSocket.sendto(ackBuf,receiveAddress)
        if receiveData<516:
            receiveFile.close()
            print("download successful")

    elif cmd == 5:
        print("error num:%d"%currentPackNum)
        break


udpSocket.close()





