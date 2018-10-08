from threading import Thread
import time

g_num = 0

def tes1():
    global g_num
    for i in range(100000):
        g_num += 1

    print("----test1----g_num=%d"%g_num)
def tes2():
    global g_num
    for i in range(100000):
        g_num += 1
    print("---test2---g_num=%d"%g_num)

if __name__ == "__main__":
    p1 = Thread(target=tes1)
    p1.start()
    p2 = Thread(target=tes2)
    p2.start()
    print(g_num)

