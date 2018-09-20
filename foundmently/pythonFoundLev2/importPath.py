import sys
import test
from imp import *
reload(test)
# 增加路径
sys.path.append(test)
print(sys.path)


import copy
a = [11,22,33]
b = [11,22,33]
c = a   #并没有创建新的空间，只是指向了一个地址（这个本质上就不算拷贝吧
e = [[11,22,33],2,3]
f = copy.copy(e)    #浅拷贝，只拷贝父对象，不会拷贝对象的内部的子对象。f[0]中存的是e[0]的指向
g = copy.deepcopy(e)    #深拷贝，拷贝对象及其子对象
e[0].append(44)
print(e ,f ,g)
print(id(e),id(f),id(g))
print(e is f ,a[0] is f[0], e is g, e[0] is g[0],id(a[0]),id(f[0]),id(g[0]))
print(id(a),id(b),id(c),a is b,a is c)   #判断内存地址

a = [11,22]
b = [33,44]
c = (a,b)
d = copy.copy(c)    #copy拷贝不可变类型时，自动判断后，一层也不拷贝
e = copy.deepcopy(c)
print(id(c),id(d),id(e))

# help(copy.copy)
# print (copy.__doc__)


#   进制转换 octal 八进制 Hexadecimal十六进制
a = 18
print(bin(a),oct(a),hex(a))
print(int("0b10010",2),int("0o22",8),int("0x12",16))

#   位运算
#   快速进行 2倍数 的乘法
a = 10
a = a<<2
print(a)
a = a>>3
print(a)

num1 = 0b110
num2 = 0b010
print(bin(num1&num2),bin(num1|num2),bin(num1 ^num2),bin(~num1),bin(~(~num1)))

#   function and val private
#   _x 单置前下划线，私有化属性或者方法，只能无法用from some_Module导入，但是可以被自己的子类和对象直接访问
#   __X double下划线，避免与子类中的属性名冲突，无法在外部直接访问，因为进行了属性名的重组name mangling //   _Class__object可以访问
#   x_ 后单置下划线，用于避免与python关键字的冲突
#   __XX__ 前后双置下划线，表示magic方法
#

class Test(object):
    def __init__(self,name = 'a'):
        self.__name = name
        self._local = "Test1Local"
    def getName(self):
        return self.__name

class testT(Test):
    def __init__(self,name):
        super().__init__(name)
    def getName2(self):
        return self.getName()
#   _Test__name
t1 = Test('bb')
print (t1.getName())
t2 = testT('cc')
print(t2.getName2(),t2._local)





##
class A(object):
    bar = 1
    def print_char(self):
        print("----f----")

    @staticmethod
    def staricPrint():
        print("static-----f----",A.bar)

    @classmethod
    def classPrint(cls):
        print("class----f----",cls.bar,cls.staricPrint())

A.staricPrint()
A.classPrint()




#   属性property
#   代替getter，setter
# class Money(object):
#     def __init__(self):
#         self.__money = 0
#     def getMoney(self):
#         return self.__money
#     def setMoney(self, value):
#         if isinstance(value, int):
#             self.__money = value
#         else:
#             print("error:不是整型数字")
# __money = property(getMoney, setMoney)

class Money(object):
    def __init__(self):
        self.__money = 0

    @property
    def money(self):
        return self.__money

    @money.setter
    def money(self, value):
        if isinstance(value, int):
            self.__money = value
        else:
            print("error:不是整型数字")

testA =Money()
# testA.__money
print( testA.money)
testA.money = 100
print(testA.money)

