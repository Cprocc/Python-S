from socket import *

serSocket = socket(AF_INET,SOCK_STREAM)
#重复使用绑定的信息
serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
localAddress = ('',7788)
serSocket.bind(localAddress)
serSocket.listen(5)

while True:
    print("---main process: waiting for the client")
    newSocket,destAddress = serSocket.accept()
    print("---main process,then to deal the data[%s]---"%str(destAddress))

    try:
        while True:
            receiveData = newSocket.recv(1024)
            if len(receiveData) > 0:
                print('receive[%s]:%s'%(str(destAddress),receiveData))
            else:
                print("[%s] client have closed"%str(destAddress))
                break
    finally:
        newSocket.close()

serSocket.close()