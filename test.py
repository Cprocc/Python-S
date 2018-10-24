# def test():
#     print('{:_^11}'.format('hello'))


# import sys
# print(sys.argv)
# sys.argv.append(45)
# print(sys.argv)

# __getattr__的调用顺序
class Bar(object):
    pass


class Foo(object):
    """"""
    def __init__(self):
        pass

    def __getattr__(self, item):
        print(item)
        return self

    # 造成递归调用
    # def __getattribute__(self, item):
    #     self.__getattribute__("hello")

    def __str__(self):
        return ""


print(Foo(). thinkDifferent.helloWorld)
