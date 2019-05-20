import _thread
from time import ctime, sleep


loops = [4, 2]


def loop(nloop, nsec, lock):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())
    lock.release()


def main():
    print('starting at:', ctime())
    locks = []
    nloops = range(len(loops))

    for _ in nloops:
        lock = _thread.allocate_lock()
        lock.acquire()
        locks.append(lock)

    print(locks)

    for i in nloops:
        _thread.start_new_thread(loop, (i, loops[i], locks[i]))

    # 一直等待，直到不满足内层while
    for i in nloops:
        while locks[i].locked():
            pass

    print('All Done at:', ctime())


if __name__ == '__main__':
    main()
