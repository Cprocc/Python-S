import threading
from time import sleep, ctime


class ThreadFunction(object):
    def __init__(self, func, args, name=''):
        self.name = name
        self.func = func
        self.args = args

    def __call__(self):
        self.func(*self.args)


def loop(nloop, nsec):
    print('start loop', nloop, 'at:', ctime())
    sleep(nsec)
    print('loop', nloop, 'done at:', ctime())


def mian():
    loops = [4, 2]
    print('starting at:', ctime())
    threads = []
    n_loops = range(len(loops))

    for i in n_loops:
        t = threading.Thread(target=ThreadFunction(loop, (i, loops[i]), loop.__name__))
        threads.append(t)

    for i in n_loops:
        threads[i].start()

    for i in n_loops:
        threads[i].join()

    print('ALL DONE at:', ctime())


if __name__ == '__main__':
    mian()

