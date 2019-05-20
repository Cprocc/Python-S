from myThread import MyThread
from time import sleep, ctime


def fib(x):
    sleep(0.005)
    if x < 2:
        return 1
    return fib(x-2) + fib(x-1)


def fac(x):
    sleep(0.1)
    if x < 2:
        return 1

    return x * fac(x-1)


def sum_1(x):
    sleep(0.1)
    if x < 2:
        return 1
    return x + sum_1(x-1)


funcs = [fib, fac, sum_1]
n = 12


def main():
    n_func = range(len(funcs))

    print('*** SINGLE THREAD')
    for i in n_func:
        print('starting', funcs[i].__name__, 'at:', ctime())
        print(funcs[i](n))
        print(funcs[i].__name__, 'finished at:', ctime())

    print('*** MULTIPLE THREADS')
    threads = []
    for i in n_func:
        t = MyThread(funcs[i], (n,), funcs[i].__name__)
        threads.append(t)

    for i in n_func:
        threads[i].start()

    for i in n_func:
        threads[i].join()
        print(threads[i].get_result())

    print('ALL DONE')


if __name__ == '__main__':
    main()
