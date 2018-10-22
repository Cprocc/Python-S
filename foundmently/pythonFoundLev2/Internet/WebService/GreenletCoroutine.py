from greenlet import greenlet
import time

def tes1():
    while True:
        print('--a--')
        gr2.switch()
        time.sleep(0.5)

def tes2():
    while True:
        print('--b--')
        gr1.switch()
        time.sleep(0.5)

gr1 = greenlet(tes1)
gr2 = greenlet(tes2)

gr1.switch()