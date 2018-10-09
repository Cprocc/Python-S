# class Student(object):
#     def __init__(self,name):
#         self.name = name

import threading

local_school = threading.local()

def processStudent():
    std = local_school.student
    print("hello,%s(in %s)"%(std,threading.current_thread().name))

def processThread(name):

    #在多线程中，用threading.local()创建出来的值，在不同线程中是分开的不会多线程共用也不会错乱
    local_school.student = name
    processStudent()

#args是parameter值，name是线程名字
#一个线程在多个函数之间互相传递
t1 = threading.Thread(target=processThread,args=('studentA',),name='ThreadA')
t2 = threading.Thread(target=processThread,args=('studentB',),name='ThreadB')

t1.start()
t2.start()
t1.join()
t2.join()