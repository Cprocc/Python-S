# def reverse(text):
#     return text[::-1]
#
# def is_palindrome(text):
#     return text == reverse(text)
#
# while True:
#     something = input("Enter text: ")
#     if something == 'exit':
#         break
#     elif is_palindrome(something):
#         print("Yes, it is a palindrome")
#     else:
#         print("No, it is not a palindrome")

# poem = '''\
# Programming is fun
# When the work is done
# if you wanna make your work also fun:
#     use Python!
# '''
#
# # 打开文件进行 'w'riting 写操作
# f = open('poem.txt', 'w')
# # 将文本写入到文件
# f.write(poem)
# # 关闭文件
#
#
# poem1 = '''\
# add something
# aaa
# '''
#
# # 将文本写入到文件
# f.write(poem1)
# f.close()
#
# f = open('poem.txt')
# # 如果没有指定文件打开方式
# # 默认使用 'r'ead 读模式
# while True:
#     line = f.readline()
#     # 零行意味着 EOF 文件结尾
#     if len(line) == 0:
#         break
#     # `line` 中已经自带换行了
#     # 因为它是从文件中读取出来的
#     print(line, end='')
# # 关闭文件
# f.close()

# import pickle
#
# # 这里我们将存储对象的文件的名称
# shop_list_file = 'shop_list.data'
# # 要买的东西的清单
# shop_list = ['apple', 'mango', 'carrot']
#
# # 写入文件
# f = open(shop_list_file, 'wb')
# # 将对象存储到文件
# pickle.dump(shop_list, f)
# f.close()
#
# # 销毁 shop_ist 变量
# del shop_list
#
# # 从存储中读回
# f = open(shop_list_file, 'rb')
# # 从文件加载对象
# stored_list = pickle.load(f)
# print(stored_list)

#encoding=utf-8
import io

f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()

text = io.open("abc.txt", encoding="utf-8").read()
print(text)