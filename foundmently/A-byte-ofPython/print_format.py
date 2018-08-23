#.format()用来规范输出
print('{0:.3f}'.format(1.0/3))
#用end控制输出结尾字符串格式，默认是换行
print('a',end='s')
print('b',end=' ')
print('what\'s your name')
print("what's you name")
print("""what"is your n'ame""")
print('this is the first\
this is the sceond')
#原始字符串
print(r'there is not have \' ')
#逻辑行和物理行
i=[1,2
   ,3]
print(2<<2,10.2//2,10.2/2)
print(5.0>3)

def shunxu(a,b=1):
    a = 2
    print(a+b)
shunxu(3,)
shunxu(b=3,a=1)

#param
def total(a=5, *numbers, **phonebook):
    '''

    :param a:一个整形参数
    :param numbers:一元数组的参数
    :param phonebook:二元数组的参数
    :return:打印这些实参
    '''
    print('a', a)

    # 遍历元组中的所有项
    for single_item in numbers:
        print('single_item', single_item)

    # 遍历字典中的所有项
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)

print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

def print_max(x, y):
    '''Prints the maximum of two numbers.

    The two values must be integers.'''
    # 如果有必要，将参数转为整数
    x = int(x)
    y = int(y)

    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')

print_max(3, 5)
print(print_max.__doc__)
help(print_max)

#sys，解释器和环境有关的包
import sys

print('The command line arguments are:')
for i in sys.argv:
    print(i)

print('\n\nThe PYTHONPATH is', sys.path, '\n')

#被导入和自己运行时执行不同的操作
if __name__ == '__main__':
    print('This program is being run by itself')
else:
    print('I am being imported from another module')


a= 1
print(dir())
del a
print(dir())

list =['a','b','c']
list1 = list[:]
del list1[0]
print(list,list1)
spanchar ='_*_'
print(spanchar.join(list))

