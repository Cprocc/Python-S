import sys
import time
import gevent

from gevent import socket,monkey
monkey.patch_all()

def handle_request(conn):
    while True:
        data = conn.recv(1024)
        if not data:
            conn.close()
            break
        print("receive:",data)
        conn.send(data)
def server(port):
    s = socket.socket()
    s.bind(('',port))
    while True:
        client,address = s.accept()
        gevent.spawn(handle_request,client)

if __name__ == '__main__':
    server(7788)