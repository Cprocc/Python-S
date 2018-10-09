import threading
import time

mutexA = threading.Lock()
mutexB = threading.Lock()
# 两个锁在两个线程中调用，但是调用的顺序不一样，通过设定超时时间来解决死锁
class myThread1(threading.Thread):
    def run(self):

        #acquire(blocking = True)
        if mutexA.acquire():
            print(self.name+'----do1---up---')
            time.sleep(1)

            if mutexB.acquire(timeout=2):
                print(self.name + '----do1---done---')
                mutexB.release()
            mutexA.release()

class myThread2(threading.Thread):
    def run(self):
        if mutexB.acquire():
            print(self.name+'----do2---up---')
            time.sleep(1)

            if mutexA.acquire(timeout=2):
                print(self.name + '----do2---done---')
                mutexB.release()
            mutexA.release()

if __name__ == "__main__":
    t1 = myThread1()
    t2 = myThread2()
    t1.start()
    t2.start()