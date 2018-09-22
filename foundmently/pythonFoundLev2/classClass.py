#类本身也是对象
class objectCreator(object):
    pass
myObject = objectCreator()
##  可以打印一个类
print(myObject)
##  可以将一个类作为参数
def echo(o):
    print (0)
print(myObject)

print (hasattr(objectCreator,"new_attribute"))
objectCreator.new_attribute = 'foo'  #为类增加属性
print (hasattr(objectCreator,"new_attribute"),objectCreator.new_attribute)
objectCreatorMirror = objectCreator
print(objectCreatorMirror,objectCreatorMirror())

def getClass(name):
    if name == "foo":
        class Foo(object):
            pass
        return  Foo
    else:
        class Bar(object):
            pass
        return Bar
myclass = getClass('foo')

##  在默认输出中，如果是类的对象会在输出中增加一行地址，而直接将类名当做对象输出时没有地址出现
##  类的类型竟然是type
print(myclass,type(myclass),myclass(),type(myclass()))

