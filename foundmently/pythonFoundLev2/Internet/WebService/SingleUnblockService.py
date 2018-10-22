# 用单一的进程，为多个client服务
from socket import *
g_socketList = []

def main():
    serSocket = socket(AF_INET, SOCK_STREAM)

    # 这里value设置为1，表示将SO_REUSEADDR标记为TRUE
    # 操作系统会在服务器socket被关闭或服务器进程终止后马上释放该服务器的端口
    # 否则操作系统会保留几分钟该端口
    serSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
    localAddress = ('',7788)
    serSocket.bind(localAddress)
    serSocket.listen(1000)
    #设置非阻塞方式
    serSocket.setblocking(False)

    while True:
        try:
            # 设置setblocking为False后，accept会有exception，所以用try接收
            # 接收客户端不堵塞
            newClientInfo = serSocket.accept()
        except Exception as result:
            pass
        else:
            print("A new client is coming:%s"%str(newClientInfo[1]))
            newClientInfo[0].setblocking(False)
            g_socketList.append(newClientInfo)
            print(len(g_socketList))

        #needDelClientInfoList用来保存所有已连接的客户端，避免已连接的没有保存
        needDelClientInfoList = []

        #为每一个已连接的客户端，收一次数据
        for clientSocket,clientAddress in g_socketList:
            try:
                receiveData = clientSocket.recv(1024)  # 接收客户端的信息不堵塞
                if len(receiveData) > 0:
                    print("receive [%s]:%s"%(str(clientAddress),receiveData))


                #在pycharm下，else中的内容未被执行，关闭连接的时候没有接受到空的字符串
                else:
                    print("client [%s] have closed"%clientAddress)
                    needDelClientInfoList.append(clientSocket)
            except Exception as result:
                pass

        # 将关闭的清空
        for needDelClientInfo in needDelClientInfoList:
            g_socketList.remove(needDelClientInfo)


if __name__ == '__main__':
    main()
