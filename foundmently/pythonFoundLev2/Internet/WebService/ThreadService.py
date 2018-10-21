from threading import Thread
from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)
#重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
localAddress = ('',7788)
serSocket.bind(localAddress)
serSocket.listen(5)

def dealWithClient(newSocket,destAddress):
    while True:
        receiveData = newSocket.recv(1024)
        #作为service，一般不主动关闭，在这里设置为当客户端关闭时关闭
        if len(receiveData) > 0:
            print('receive[%s]:%s'%(str(destAddress),receiveData))
        else:
            print('[%s]client have closed'%str(destAddress))
            break
    newSocket.close()

def main():

    serSocket = socket(AF_INET,SOCK_STREAM)   #用来等待新的客户端到来
    serSocket.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
    localAddress = ('',7788)
    serSocket.bind(localAddress)
    serSocket.listen(5)
    try:
        while True:
            print('----main process,wait the new process----')
            newSocket,destAddress = serSocket.accept()  #newSocket 是一个可活动的client套接字
            print('----main process,create a new process to deal the')

            #创建client进程
            client = Thread(target=dealWithClient,args=(newSocket,destAddress))
            client.start()

            # newSocket.close()
    finally:
        serSocket.close()

if __name__ == 'main':
    main()