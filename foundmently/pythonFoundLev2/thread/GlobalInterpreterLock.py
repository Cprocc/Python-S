# 多核cpu，假多线程
# gil只能保证一个线程在执行
# 进程可以占多个cpu，进程效率高于多线程，尤其是多核
# 用c语言实现关键代码实现真多线程


#将多核cpu跑满
from ctypes import *
from threading import Thread
# gcc loop.c -shared -o libXXXXX.so
lib = cdll.LoadLibrary("./libDeadLoop.so")

t = Thread(target=lib.DeadLoop)
t.start()

while True:
    pass