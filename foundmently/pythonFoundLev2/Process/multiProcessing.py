import multiprocessing as mp
import os

##linux 下用fork创建的子进程，可以比父进程结束的更早
##用process创建的子进程，则不会
##Process([group [, target [, name [, args [, kwargs]]]]])

def job(q):
    res = 0
    for i in range(1000):
        res += i+i**2+i**3
    q.put(res) # queue
    print("self id",os.getpid(),"parentsId",os.getppid())

if __name__ == '__main__':
    print("self id：",os.getpid(),"parentsId",os.getppid())
    #创建进程队列
    q = mp.Queue()
    p1 = mp.Process(target=job, args=(q,))
    p2 = mp.Process(target=job, args=(q,))
    p1.start()
    p2.start()
    print(p1.is_alive())
    print(p2.is_alive())

    #join代表只有当前进程执行完毕，才会向下
    #.join([timeout]) timeout参数，可选项，代表最长的等待时间。

    p1.join()
    p2.join()
    res1 = q.get()
    res2 = q.get()
    print(res1,res2,res1+res2)