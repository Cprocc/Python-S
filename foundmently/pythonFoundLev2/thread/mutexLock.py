from threading import Thread,Lock
import time

g_num = 0

def tes1():
    global g_num
    for i in range(1000000):
        mutexFlag = mutex.acquire(True) #进入locked状态，acquire(blocking) blocking参数，True当前线程会阻塞
        if mutexFlag:
            g_num += 1
            mutex.release() #释放后锁进入unlocked状态，接下来从同步阻塞的线程中调用一个来获得锁
    print("---test1---g_num = %d"%g_num)

def tes2():
    global g_num
    for i in range(1000000):

        #是以通知的方式还是轮询//  通知
        # mutexFlag = mutex.acquire(False)
        mutexFlag = mutex.acquire(True) #试图调用锁时被阻塞
        if mutexFlag:
            g_num += 1
            mutex.release()
    print("---test2---g_num = %d"%g_num)



mutex = Lock()

p1 = Thread(target=tes1)
p1.start()

p2 = Thread(target=tes2)
p2.start()

print("---g_num = %d---"%g_num)