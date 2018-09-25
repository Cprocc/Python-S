#coding = utf-8
import sys
a = "hello"
b = a
list1 = [a,a]
del b
del list1
print(sys.getrefcount(a))

import  gc
class ClassA():
    def __init__(self):
        print("object born,id%s"%str(hex(id(self))))
    # def __del__(self):
    #     print('object del,id:%s'%str(hex(id(self))))

def f2():
    while True:
        c1 = ClassA()
        c2 = ClassA()
        c1.t = c2
        c2.t = c1
        del c1
        del c2

def f3():
    print("program starting")
    print(gc.collect())
    c1 = ClassA
    c2 = ClassA
    c1.t = c2
    c2.t = c1
    print('init finish')
    del c1
    del c2
    print('delete finish')
    print(gc.garbage)
    print('-'*20)
    print(gc.collect())  #显式执行垃圾回收
    print('-'*20)
    print(gc.garbage)
    print('finish'*3)


if __name__ =='__main__':
    gc.set_debug(gc.DEBUG_LEAK)  #设置gc模块的日志
    f3()

