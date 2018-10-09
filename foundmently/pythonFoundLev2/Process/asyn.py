from multiprocessing import Pool
import time
import os

def tes1():
    print("---process in pool--- pid=%d,ppid=%d--"%(os.getpid(),os.getppid()))
    for i in range(3):
        print('---%d---'%i)
        time.sleep(1)
    return "tes1over"

def tes2(args):
    print("---callBack function-- pid=%d"%os.getpid())
    print('---callBack function--args=%s'%args)

if __name__ == "__main__":
    pool = Pool(3)
    pool.apply_async(func=tes1,callback=tes2)

    for i in range(10):
        time.sleep(0.4)
        print('---main process pid=%d has finished'%os.getpid())