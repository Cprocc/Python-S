###自定义元类

# 1. Foo中有__metaclass__这个属性吗？ 如果是， Python会通过__metaclass__创建⼀个名字为Foo的类(对象)
# 2. 如果Python没有找到__metaclass__， 它会继续在Bar（⽗类） 中寻找 __metaclass__属性， 并尝试做和前⾯同样的操作。
# 3. 如果Python在任何⽗类中都找不到__metaclass__， 它就会在模块层次中去寻找__metaclass__， 并尝试做同样的操作。
# 4. 如果还是找不到__metaclass__,Python就会⽤内置的type来创建这个类对象

##可以在__metaclass__中放置些什么代码呢？可以创建一个类的东西:type,使用到type或者子类化type的东西
def upper_attr(future_class_name, future_class_parents, future_class_attr):

    #遍历属性字典，把不是__开头的属性名字变为大写
    newAttr = {}
    for name,value in future_class_attr.items():
        if not name.startswith("__"):
            newAttr[name.upper()] = value

    #调用type来创建一个类
    return type(future_class_name, future_class_parents, newAttr)

class Foo(object,metaclass=upper_attr):
    bar = 'bip'

print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))

f = Foo()
print(f.BAR)

class UpperAttrMetaClass(type):
    def __new__(clscls, future_class_name, future_class_parents, future_class_attr):
        newAttr = {}
        for name, value in future_class_attr.items():
            if not name.startswith("__"):
                newAttr[name.upper()] = value
        return type(future_class_name, future_class_parents, newAttr)
class Foo(object,metaclass=UpperAttrMetaClass):
    bar = 'bip'
print(hasattr(Foo, 'bar'))
print(hasattr(Foo, 'BAR'))
f = Foo()
print(f.BAR)