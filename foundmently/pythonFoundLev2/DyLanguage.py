# 定义的时候没有 运行的时候可以添加,动态可适应变化
##给对象 //而非类  添加属性
class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age

a = Person("a",10)
a.addR = "beijing"
print(a.addR)

## 给类添加属性
Person.num = 100
print(a.num)

##添加方法,不能像属性那样添加 types.
def run(self,speed):
    print(a.name," move speed ",speed)
import types
a.run = types.MethodType(run,a)   #绑定在class Person内部
a.run(100)

xxx = types.MethodType(run,a)   #绑定给任意函数
xxx(1000)

##静态方法
@staticmethod
def tes1():
    print("--tes1--")

Person.tes1 = tes1
Person.tes1()

##类方法
@classmethod
def printNum(cls):
    print("---class---")

Person.printNum = printNum
Person.printNum()

## __slots__不允许添加属性
print(dir(a))
class PersonS(object):
    __slots__ = ("name","age")

p = PersonS()
p.name ="wang"
p.age = 10
# p.addr = 'beijing'  这个就不能添加成功
print(dir(p))

