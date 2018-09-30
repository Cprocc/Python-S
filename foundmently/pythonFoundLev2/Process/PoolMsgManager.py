from multiprocessing import Manager,Pool
import os,time,random


# 使用Pool,进行进程间通信的时候，用Manager
def reader(q):
    print("reader starting(%s),father process is(%s)"%(os.getpid(),os.getppid()))
    for i in range(q.qsize()):
        print('reader get msg from Queue:%s'%q.get(True))

def writer(q):
    print("writer starting(%s),father process is(%s)"%(os.getpid(),os.getppid()))
    for i in "PythonStudy":
        q.put(i)

if __name__ == "__main__":
    print("(%s)start"%os.getpid())
    q = Manager().Queue()
    po = Pool()
    po.apply(writer,(q,))
    po.apply(reader,(q,))
    po.close()
    po.join()
    print("(%s) End"%os.getpid())
