from socket import *

conNum = input("input the time of connect Service")
for i in range(int(conNum)):
    s = socket(AF_INET,SOCK_STREAM)
    s.connect(("127.0.0.1",7788))
    print(i)