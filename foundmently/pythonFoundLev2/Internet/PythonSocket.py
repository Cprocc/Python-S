# import socket
# # socket.AF_INET //ipv4协议,socket.SOCK_STREAM // tcp协议，socket.SOCK_DGRAM // udp协议
#
# s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# 解决python3的内容错误
# str.encode("utf-8"),将字符串转换为utf-8类型
from socket import *

udpSocket = socket(AF_INET,SOCK_DGRAM)

# 表示特定的端口就可以发送给指定的程序，如飞秋：2425 socket唯一标识网络中的计算机的进程
sendAddress = ('192.168.56.1',8080)

while True:
    sendData = input("input your send msg:")

    # 接收方每次收到的端口可能不一样，我们测试的网络调试程序用的是gb2312码
    udpSocket.sendto(sendData.encode("gb2312"),sendAddress)


udpSocket.close()
