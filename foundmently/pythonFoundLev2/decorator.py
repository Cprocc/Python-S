## 闭包
def closePackage(number):
    print("----1----",number)
    def closePackage2(number):
        print("----2----")
        number +=100
        print(number)
    return  closePackage2

closePackage(100)
clo = closePackage(100)
clo(100)
clo(200)

## 利用闭包，构建线性方程
def lineConst(a,b):
    def lineVal(x):
        return  a*x + b
    return lineVal
line1 = lineConst(1,2)
line2 = lineConst(2,1)
print(line1(2))
print(line2(2))


##装饰器预备,第二次会覆盖第一次的内容。等于重新定义了foo这个函数对象
def foo():
    print("--foo1--")
def foo():
    print("--foo2--")
foo = lambda x:x+1
foo(1)

##  装饰器 decorator
def verification(func):
    def inner():
        print("--verification now--")
        func()
    return inner

@verification  #增加语法糖
def f1():
    print("--doing f1--")
@verification
def f2():
    print("--doing f2--")

f1()
f2()
# innerFunction = verification(f1) ##拿到inner函数的地址
# innerFunction()
# ###根据上一个例子 我们可以重新定义f1，指向innerFunction
# f1 = verification(f1)
# f1()

## decorator
def makeBold(fn):
    def wrapped():
        return "<b>" + fn() +"</b>"
    return wrapped
def makeItalic(fn):
    def wrapped():
        return "<i>" + fn() +"</i>"
    return wrapped

@makeBold
def tes1():
    return "hello 1"
@makeItalic
def tes2():
    return "hello 2"

## 调用过程和@顺序相同，和装饰顺序相反
@makeBold
@makeItalic
def tes3():
    return "hello 3"
print(tes1())
print(tes2())
print(tes3())

## 装饰器的装饰工作时间
def w1(func):
    print("---正在装饰---")
    def inner():
        print("---正在验证权限---")
        func()  #只有加了这个命令，被装饰的才会被调用
    return inner
@w1  # 在python解释器工作的时候w1就开始进行装饰了，而不用再调用w1,正在装饰就会被输出
def f1():
    print("---1---")
f1()

def w1(func):
    print("-------装饰1------")
    def inner():
        print("-----正在验证权限1------")
        func()
    return  inner
def w2(func):
    print("-------装饰2------")
    def inner():
        print("-----正在验证权限2------")
        func()
    print("--when to jump--")
    return  inner
@w1  # f1 = w1(f1)
@w2
def f1():
    print("--验证过的内容被执行--")
f1()

## 有参数函数进行装饰,不定长参数进行装饰
# def func(functionName):
#     print("--func1--")
#     #def funcIn(a,b):
#     def funcIn(*args,**kwargs):
#         print("---funcIn---1---")
#         #functionName(a,b)
#         functionName(*args,**kwargs)
#         print("---funcIn---2---")
#     print("---func---2---")
#     return  funcIn
#
# @func
# def tes(a,b):
#     print("----test--a=%d,b=%d"%(a,b))
# tes(1,2)


##  带有返回值的装饰器
# def func(functionName):
#     print("--func1--")
#     #def funcIn(a,b):
#     def funcIn():
#         print("---funcIn---1---")
#         #functionName(a,b)
#         re = functionName()
#         print("---funcIn---2---")
#         return re
#     print("---func---2---")
#     return  funcIn
#
# @func
# def tes():
#     print("----test----")
#     return "return"
# print(tes())

##使用通用装饰器
# def func(functionName):
#
#     def func_in(*args,**kwargs):
#         print("----record--------------------------------")
#         ret = functionName(*args,**kwargs)
#         return ret
#
#     return func_in
#
# @func
# def tes():
#     print("---testHaveReturn---")
#     return "return"
#
# @func
# def tes2():
#     print("---testWithoutReturn---")
#
# @func
# def tes3(a):
#     print(a)
#
# ret = tes()
# print(ret)
# tes2()
# tes3(11)

## 装饰器带参数
def funcArg(arg):
    def func(functionName):
        def funcIn():
            print("---------------record-------",arg)
            functionName()
        return funcIn
    return func
@funcArg("IhaveVal")
def tes():
    print("---test-----")
tes()

##类装饰器
class Test(object):
    def __init__(self,func):  ##这里的func传过来的值是tes1
        print("初始化")
        print(func.__name__)
        self.__func = func
    def __call__(self, *args, **kwargs):
        print("call me")
        self.__func()

@Test #tes1 = Test(tes1)
def tes1():
    print("----test----")
tes1()
