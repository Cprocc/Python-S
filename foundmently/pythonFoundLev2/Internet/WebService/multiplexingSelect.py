import select
import socket
import sys

#多路复用，不使用多线程多进程
#select 检测套接字的当前状况,返回可以收发的，封装在底层，效率要高
#select 监听队列的默认大小1024/32位，2048/64位  检测方式是轮询

serSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serSocket.bind(('',7788))
serSocket.listen(5)

inputs = [serSocket, sys.stdin]

while True:

    #三个套接字的作用
    # 1 检测这个列表中的套接字是否可以接收数据
    # 2 检测这个套接字可否发数据
    # 3 检测这个套接字是否发生了异常
    readAble,writeAble,exceptional = select.select(inputs,[],[])

    for sock in readAble:
        # 监听活动端口中，可接受信息的socket

        if sock == serSocket:
            conn, address = serSocket.accept()
            inputs.append(conn)

        elif sock == sys.stdin:
            cmd = sys.stdin.readline()
            running = False
            break
        else:
            data = sock.recv(1024)
            if data:
                sock.send(data)
            else:
                inputs.remove(sock)
                sock.close()

        if  running == False:
            break

serSocket.close()