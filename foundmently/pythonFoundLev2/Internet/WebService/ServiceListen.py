from time import sleep
from socket import *

tcpSerSocket = socket(AF_INET,SOCK_STREAM)

address = ('',7788)
tcpSerSocket.bind(address)

#listen 半连接和已连接里面做多有connNum 个
connNum = int(input("the largest number of connection"))

tcpSerSocket.listen(connNum)

for i in range(10):
    print(i)
    sleep(1)

print("time loading over")

while True:


    newSocket,clientAddress = tcpSerSocket.accept()   #取出一个，才能继续连接下一个
    print(clientAddress)
    sleep(1)

