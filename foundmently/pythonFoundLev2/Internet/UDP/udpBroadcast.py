import socket,sys
dst = ("<broadcast>",8080)
s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

#发送广播数据
s.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,1)

s.sendto(b"Hi",dst)

print("等待对方回复")

while True:
    (buf,address) = s.recvfrom(2048)
    print("Received from %s:%s"%(address,buf))
    if buf.decode('utf-8') == 'exit':
        break

s.close()