import threading
import time

class myThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'am"+self.name + '@' +str(i)
            print(msg)

#主线程不会先结束，因为要回收内存空间之类的东西
#unix进程为0,1，0用来调度，1用来创建
if __name__ == "__main__":
    t = myThread()
    t.start()