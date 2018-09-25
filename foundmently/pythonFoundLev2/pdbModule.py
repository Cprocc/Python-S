#coding = utf-8
import pdb

### pdb
# l 显示当前调用过程中的代码
# n 执行下一行代码
# p name 查看当前变量的值 p表示打印

# a = 'aaa'
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# final = a+b+c
# print(final)


### 当程序中有两个pdb.set_trace()
# c 让程序执行到下一个pdb.set_trace()

# a = 'aaa'
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# pdb.set_trace()
# final = a+b+c
# print(final)


###
# b line 在某行处设置断点 代替pdb.set_trace
# s 进入到这个函数并且停止
# l 列出这个函数
# n 在函数内部执行下一句
# a 查看传进函数的所有参数
# r 执行到函数的最后一步

# def combineM(s1,s2):
#     s3 = s1 + s2
#     s3 = ' " ' + s3 + ' " '
#     return s3
#
# a = 'aaa'
# pdb.set_trace()
# b = 'bbb'
# c = 'ccc'
# final = combineM(a,b)
# print(final)

###
# ！ arg = 100 修改变量的方法

# def pdb_test(arg):
#     for i in range(arg):
#         print(i)
#     return  arg
# pdb.run("pdb_test(10)")


###
#
def add3Nums(a1,a2,a3):
    result: a1+a2+a3
    return  result
def get3NumsAverage(s1,s2):
    s3 = s1+s2+s1
    result  = 0
    result = add3Nums(s1,s2,s3)/3
    return result
if __name__ =="__main__":
    a = 11
    pdb.set_trace()
    b = 12
    final = get3NumsAverage(a,b)
    print(final)