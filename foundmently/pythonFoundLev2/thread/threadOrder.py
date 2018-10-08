import threading
import time

class myThread(threading.Thread):
    def run(self):
        for i in range(3):
            time.sleep(1)
            msg = "I'm"+self.name+"@"+str(i)
            print(msg)

#线程的执行顺序和生成顺序没有绝对的关系，主要是操作系统的调度算法决定的
def test():
    for i in range(5):
        t = myThread()
        t.start()
if __name__ == "__main__":
    test()