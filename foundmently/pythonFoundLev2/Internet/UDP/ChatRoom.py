from threading import Thread
from socket import *

def receiveData():
    while True:
        receiveInfo = udpSocket.recvfrom(1024)
        print("\r>>%s:%s" % (str(receiveInfo[1]), receiveInfo[0].decode('gb2312')))

def sendData():
    while True:
        sendInfo = input("<<")
        udpSocket.sendto(sendInfo.encode('gb2312'),(Ip,Port))

udpSocket = None
Ip = ""
Port = 0
def main():
    global udpSocket,Ip,Port

    Ip = input('对方的ip')
    Port = int(input('对方的port'))

    udpSocket = socket(AF_INET, SOCK_DGRAM)
    udpSocket.bind(('',4444))

    Tr = Thread(target=receiveData)
    Ts = Thread(target=sendData)

    Tr.start()
    Ts.start()

    Tr.join()
    Ts.join()

if __name__ == "__main__":
    main()
