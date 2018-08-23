# try:
#     text = input('Enter something --> ')
# except EOFError:
#     print('Why did you do an EOF on me?')
# except KeyboardInterrupt:
#     print('You cancelled the operation.')
# else:
#     print('You entered {}'.format(text))

# class ShortInputException(Exception):
#     '''用户定义的异常对象'''
#     def __init__(self, length, atleast):
#         Exception.__init__(self)
#         self.length = length
#         self.atleast = atleast
#
# try:
#     text = input('Enter something --> ')
#     if len(text) < 3:
#         raise ShortInputException(len(text), 3)
#     # 其他程序可以在这里正常执行
# except EOFError:
#     print('Why did you do an EOF on me?')
# except ShortInputException as ex:
#     print(('ShortInputException: The input was ' +
#            '{0} long, expected at least {1}')
#           .format(ex.length, ex.atleast))
# else:
#     print('No exception was raised.')

# import sys
# import time
#
# f = None
# try:
#     f = open("poem.txt",'w')
#     # 我们通常读取文件的语句
#     while True:
#         line = f.readline()
#         if len(line) == 0:
#             break
#         print(line, end='')
#         sys.stdout.flush()
#         print("Press ctrl+c now")
#         # 让程序保持运行一段时间
#         time.sleep(2)
# except IOError:
#     print("Could not find file poem.txt")
# except KeyboardInterrupt:
#     print("!! You cancelled the reading from the file.")
# finally:
#     if f:
#         f.close()
#     print("(Cleaning up: Closed the file)")
# with open("poem.txt") as f:
#     for line in f:
#         print(line, end='')
#
# import sys
# print(sys.version_info)
#
# import os
# import platform
# import logging
#
# if platform.platform().startswith('Windows'):
#     logging_file = os.path.join(os.getenv('HOMEDRIVE'),
#                                 os.getenv('HOMEPATH'),
#                                 'test.log')
# else:
#     logging_file = os.path.join(os.getenv('HOME'),
#                                 'test.log')
#
# print("Logging to", logging_file)
#
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s : %(levelname)s : %(message)s',
#     filename=logging_file,
#     filemode='w',
# )
#
# logging.debug("Start of the program")
# logging.info("Doing something")
# logging.warning("Dying now")

points = [{'x': 2, 'y': 3},
          {'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

