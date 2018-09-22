L = [x*2for x in range(5)]
LL = (x*2 for x in range(5))
print(L,LL,next(LL),next(LL),"----------------------")
for x in LL:
    print(x)

##  利用yield生成generator
##
def fib(times):
    n = 0
    a,b = 0,1
    while n<times:
        yield b
        a,b = b,a+b
        n+=1
    return 'done'

g = fib(5)  ## 加了yield，函数则为generator，在调用的时候不会执行
g1 = g
print(id(g), id(g1))
for i in g:
    print(i)
while True:
    try:
        x = next(g1) ## 等价于g1.__next__()
        print("value:%d"%x)
    except StopIteration as e:
        print("⽣成器返回值:%s"%e.value)
        break

def gen():
    i = 0
    while i<5:
        temp = yield i
        print(temp)
        i+=1
t = gen()
print (t.__next__(),t.__next__(),t.__next__(),t.__next__(),next(t))


##  用yield控制多任务协成执行
# def test1():
#     while True:
#         print("--------1--------")
#         yield None
# def test2():
#     while True:
#         print("--------2--------")
#         yield None
#
# t1,t2 = test1(),test2()
# 多任务执行方式，协成执行
# while True:
#     print("--------0--------")
#     t1.__next__()
#     t2.__next__()
from collections import Iterable
from collections import Iterator
#iterable interator
for a in "print":
    print(a)

print(isinstance([],Iterable))
print(isinstance([],Iterator))
print(isinstance(iter([]),Iterator))