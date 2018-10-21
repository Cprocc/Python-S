from socket import *
import time
g_socketList = []

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddress = ('',7788)
    serSocket.bind(localAddress)
    serSocket.listen(1000)
    #设置非阻塞方式
    serSocket.setblocking(False)

    while True:
        try:
            newClientInfo = serSocket.accept()
        except Exception as result:
            pass
        else:
            print("A new client is coming:%s"%str(newClientInfo))
            newClientInfo[0].setblocking(False)
            g_socketList.append(newClientInfo)

        needDelClientInfoList = []

        for clientSocket,clientAddress in g_socketList:
            try:
                receiveData = clientSocket.recv(1024)
                if len(receiveData) > 0:
                    print("receive [%s]:%s"%(str(clientAddress),receiveData))
                else:
                    print("client [%s] have closed"%clientAddress)
                    needDelClientInfoList.append(clientSocket)
            except Exception as result:
                pass

        for needDelClientInfo in needDelClientInfoList:
            needDelClientInfoList.remove(needDelClientInfo)

if __name__ == '__main__':
    main()
