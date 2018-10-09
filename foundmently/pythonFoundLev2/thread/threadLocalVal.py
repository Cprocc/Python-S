import threading
import time

class myThread(threading.Thread):
    def __init__(self,num,sleepTime):
        threading.Thread.__init__(self)
        self.num = num
        self.sleepTime = sleepTime
    def run(self):
        self.num += 1
        time.sleep(self.sleepTime)
        print("线程(%s),num = %d"%(self.name,self.num))

if __name__ == "__main__":
    mutex = threading.Lock()
    t1 = myThread(100,5)
    t1.start()
    t2 = myThread(200,1)
    t2.start()

# def tes1():
#     name = threading.current_thread().name
#     print("---thread name is %s---"%name)
#     g_num = 100
#     if name == "Thread-1":
#         g_num += 1
#     else:
#         time.sleep(2)
#     print("---thread is %s---g_num=%d"%(name,g_num))
#
# p1 = threading.Thread(target=tes1)
# p1.start()
# p2 = threading.Thread(target=tes1)
# p2.start()