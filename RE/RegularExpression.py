import re
# 正则表达式
# result = re.match("hello", "helloWorld")
# print(result.group())


def re_phone_number(char_number):
    result = re.match("^1[34578][0-9]{9}$", char_number)
    # result.group()
    print(result)


def main():
    re_phone_number("15927278131")
    re_phone_number("159272781311")
    re_phone_number("258")


if __name__ == '__main__':
    main()
    r = re.match("\d*", "a")
    print(r.group())  # 输出这一行的结果是一个空字符串
