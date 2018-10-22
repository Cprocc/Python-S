# 解决了select监听队列大小上限的问题
#不再适用select 和poll 轮询的方式，采用时间通知机制

from socket import *
import select

s = socket(AF_INET,SOCK_STREAM)
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)
s.bind(("",7788))
s.listen(10)

epoll = select.epoll()

# 当epoll检测到描述符事件发⽣并将此事件通知应⽤程序， 应⽤程序必须⽴即处理该事件
# 当epoll检测到描述符事件发⽣并将此事件通知应⽤程序， 应⽤程序可以不⽴即处理该事件
epoll.register(s.fileno(),select.EPOLLIN|select.EPOLLET)

connections = {}
addresses = {}

#文件描述符

while True:

    #poll方法，拿到列表
    epoll_list = epoll.poll()

    #fd文件描述符，events该描述符对应的时间
    for fd,events in epoll_list:
        if fd == s.fileno():
            conn,addr = s.accept()
            print("---new client coming%s ---"%str(addr))

            connections[conn.fileno()] = conn
            addresses[conn.fileno()] = addr
            epoll.register(conn.fileno(), select.EPOLLIN | select.EPOLLET)

        # EPOLLIN判断是否可以接数据
        elif events == select.EPOLLIN:

            # 根据文件描述符找到套接字
            receiveData = connections[fd].recv(1024)

            if len(receiveData) > 0:
                print("receive:%s"%receiveData)
            else:
                epoll.unregister(fd)
                connections[fd].close()
                print("%s---offline---"%str(addresses[fd]))
