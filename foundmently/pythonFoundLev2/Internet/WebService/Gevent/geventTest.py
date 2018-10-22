import gevent


# gevent遇到耗时操作，gevent会自动把控制权交出去
def f(n):
    for i in range(n):
        print(gevent.getcurrent(),i)
        gevent.sleep(1)

g1 = gevent.spawn(f,5)
g2 = gevent.spawn(f,5)
g3 = gevent.spawn(f,5)
g1.join()
g2.join()
g3.join()