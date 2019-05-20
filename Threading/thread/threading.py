# 守护线程
# 非守护线程 thread.setDeamon(True),表示这个线程不重要

import threading
from time import sleep, ctime

loops = [4, 2]


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def main():
    print('starting at:', ctime())
    threads = []
    nloops = range(len(loops))

    for i in nloops:
        t = threading.Thread(target=loop, args=(i, loops[i]))
        threads.append(t)

    for i in nloops:
        threads[i].start()

    for i in nloops:
        # join 会等到线程结束，或者在给定了timeout()参数的时候，等到超时为止
        threads[i].join()

    print('ALL DONE at:', ctime())


if __name__ == '__main__':
    main()
