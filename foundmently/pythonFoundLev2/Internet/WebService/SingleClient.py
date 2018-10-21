from socket import *
import random
import time

serviceIp = input("Input the ip of server")
connNum = input("Input the time of connection")
g_socketList = []

for i in range(int(connNum)):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect((serviceIp,7788))
    g_socketList.append(s)
    print(i)

def main():
    while True:
        for s in g_socketList:
            data = (random.randint(1,100))
            s.send(data)

