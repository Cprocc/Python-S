from multiprocessing import Process
import time
import os

class Process_Class(Process):
    def __init__(self,interval):
        Process.__init__(self)
        self.interval = interval

    def run(self):
        print("子进程(%s)开始执行，父进程为(%s)"%(os.getpid(),os.getppid()))
        t_start = time.time()
        time.sleep(self.interval)
        t_stop = time.time()
        print("(%s)执行结束，耗时%0.2fsecond"%(os.getpid(),t_stop-t_start))

if __name__ == "__main__":
    t_start = time.time()
    print("当前程序进程(%s)"%os.getpid())
    #通过Process类来创建进程
    p1 = Process_Class(2)
    p1.start()
    p1.join()
    t_stop = time.time()
    print("(%s)执行结束，耗时%0.2fsecond"%(os.getpid(),t_stop-t_start))