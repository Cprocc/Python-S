#__getattr__(self,name):访问不存在属性时调用
#__getattribute__(self,name):访问存在的属性时调用，先调用该方法查看属性是否存在，若不存在，调用__getattr__
#__setattr__(self,name,value):
#__delattr__(self,name):

class Person(object):
    pass
print(dir(Person))

class Study(object):
    def __init__(self,subject1):
        self.subject1 = subject1
        self.subject2 = 'cpp'
    # 属性访问时拦截器，打log
    def __getattribute__(self, obj):
        print("-----1>%s"%obj)
        if obj == 'subject1':
            print('log subject1')
            return 'redirect python'
        else:
            temp = object.__getattribute__(self,obj)
            print("-----2>%s"%str(temp))
            return temp
    def show(self):
        print('this is the class')

s = Study("python")
print(s.subject1)
print(s.subject2)
s.show()

class Test:
    def __getattr__(self, name):
        print('__getattr__')

    def __getattribute__(self, name):
        print('__getattribute__')

    def __setattr__(self, name, value):
        print('__setattr__')

    def __delattr__(self, name):
        print('__delattr__')

t=Test()
t.x

###
# 首先访问 __getattribute__() 魔法方法（隐含默认调用，无论何种情况，均会调用此方法）
#
# ② 去实例对象t中查找是否具备该属性： t.__dict__ 中查找，每个类和实例对象都有一个 __dict__ 的属性
#
# ③ 若在 t.__dict__ 中找不到对应的属性， 则去该实例的类中寻找，即 t.__class__.__dict__
#
# ④ 若在实例的类中也招不到该属性，则去父类中寻找，即 t.__class__.__bases__.__dict__中寻找
#
# ⑤ 若以上均无法找到，则会调用 __getattr__ 方法，执行内部的命令（若未重载 __getattr__ 方法，则直接报错：AttributeError)
#
# 以上几个流程，即完成了属性的寻找。
#
# 一旦重载了 __getattribute__() 方法，如果找不到属性，则必须要手动加入第④步，否则无法进入到 第⑤步 (__getattr__)的。
class Test:
    def __getattr__(self, name):
        print('__getattr__')

    def __getattribute__(self, name):
        print('__getattribute__')
        object.__getattribute__(self, name)
        # super().__getattribute__(name)

    def __setattr__(self, name, value):
        print('__setattr__')

    def __delattr__(self, name):
        print('__delattr__')

t = Test()
t.x

###
#__getattribute__的坑
class Person(object):
    def __getattribute__(self, item):
        print("---test---")
        if item.startswith("a"):
            return  "a_first"

    def test(self):
        print('what_first')

z = Person()
print(z.a)

#print(z.b)
##会让程序死掉
#原因是： 当t.b执⾏时， 会调⽤Person类中定义的__getattribute__⽅法， 但是在
#if条件不满⾜， 所以 程序执⾏else⾥⾯的代码， 即return self.test 问题就在
#self.test的值返回， 那么⾸先要获取self.test的值， 因为self此时就是t这个对象
#t.test 此时要获取t这个对象的test属性， 那么就会跳转到__getattribute__⽅法
#⽣了递归调⽤， 由于这个递归过程中 没有判断什么时候推出， 所以这个程序会永⽆休⽌
#每次调⽤函数， 就需要保存⼀些数据， 那么随着调⽤的次数越来越多， 最终内存吃光，
# 注意： 以后不要在__getattribute__⽅法中调⽤self.xxxx