print(dir(__builtins__))

def f1( x, y ):
    return (x,y)
l1 = [ 0, 1, 2, 3, 4, 5, 6 ]
l2 = [ 'Sun', 'M', 'T', 'W', 'T', 'F', 'S' ]
l3 = map( f1, l1, l2 )
print(list(l3))

###filter
#function:接受⼀个参数， 返回布尔值True或False
#sequence:序列可以是str， tuple， list
#filter(function, iterable)
a = filter(lambda x:x%2,[1,2,3,4])
b = filter(None,'she')
print(list(a),list(b))

###set
#y&z
#x|y
#x-y

###functools
import functools
print(dir(functools))

def showArg(*args,**kwargs):
    print(args)
    print(kwargs)
# 把一个函数的某些参数设置成为默认值，返回一个新的函数，调用这个新函数会更简单args(),kwarg{}
p1 = functools.partial(showArg,1,2,3)
p1()
p1(4,5,6)
p1(a='python',b='cpp')

p2 = functools.partial(showArg,a= 3,b = 'linux')
p2()
p2(1,2)
p2(a = 'python',b = 'cpp')

###warps 函数
#普通装饰器，装饰之后函数其实已经变为了另外一个
def note(func):
    "note function"
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper
@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)

#warps用于消除装饰器的副作用
def note(func):
    "note function"
    @functools.wraps(func)
    def wrapper():
        "wrapper function"
        print('note something')
        return func()
    return wrapper
@note
def test():
    "test function"
    print('I am test')

test()
print(test.__doc__)