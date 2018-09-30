from multiprocessing import Process,Queue
import os,time,random


# Queue 只能用于process创建的进程进行通讯
def write(q):
    for value in ['A','B','C']:
        print('Put %s to queue...'%value)
        q.put(value)
        time.sleep(random.random())
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print('Get %s from queue.'%value)
            time.sleep(random.random())
        else:
            break

if __name__ == '__main__':

    #两个进程同时对一个进行操作
    #只有一个发送方，和一个接收方

    q = Queue()  #no parameter
    pw = Process(target=write,args=(q,))
    pr = Process(target=read,args=(q,))
    pw.start()
    pw.join()
    pr.start()
    pr.join()
    print(' ')
    print('all date have written')