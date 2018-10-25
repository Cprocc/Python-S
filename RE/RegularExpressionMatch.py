import re
# 正则表达式
# result = re.match("hello", "helloWorld")
# print(result.group())


# 通过match进行匹配
def re_phone_number(char_number):
    result = re.match("^1[34578][0-9]{9}$", char_number)
    # result.group()
    print("phone number is " + str(result))


def re_hundred_number(number):
    result = re.match(r"[1-9]\d?$|0$|100$", number)
    print("the number which small than 100 is " + str(result))


def re_html_road(html_char):
    # result = re.match(r"<(.+)><(.+)>.+</\2></\1>", html_char)
    result = re.match(r"<(?P<html>.+)><(?P<h1>.+)>.+</(?P=h1)></(?P=html)>", html_char)
    print("the html match result is " + str(result))


def re_mail(mail_char):
    result = re.match(r"(\w+)@(163|126|qq|gmail|foxmail)\.(com|cn|net)", mail_char)
    print("the mail match result is" + str(result))
    print(result.group())


# 对match的校验
def match_main():
    print("-"*50 + "phone number")
    re_phone_number("15927278131")
    re_phone_number("159272781311")
    print("-"*50 + "number smaller than 100")
    re_hundred_number("100")
    re_hundred_number("333")
    print("-"*50 + "body of html")
    re_html_road("<html><h1>hello web</h1></html>")
    re_html_road("<html><h1>hello web</h1></htm>")
    print("-"*50 + "mail")
    re_mail("755516806@qq.com")
    re_mail("xinchengzhao7@gmail.com")


# 通过search进行匹配,拿到第一个检查就结束
def search_html_char(char):
    # result = re.search(r"hello", char)
    result = re.search(r"^<html><h1>(hello)", char)
    print(result.group(1))


# 通过findall进行匹配
def findall_html_char(char):
    result = re.findall(r"<h1>(\w+)</h1>", char)
    print(result)


# search的校验
def search_findall_main():
    # html_1 = "<html><h1>hello re.Search</h1></html>"
    html_2 = "<html><h1>helloH1</h1><h1>helloH2</h1></html>"
    # search_html_char(html_1)
    findall_html_char(html_2)


def add(temp):
    str_num = temp.group()
    # print(temp.group(), type(temp), type(temp.group()))
    num = int(str_num) + 1
    return str(num)


def sub_main():
    ret = re.sub(r"hello", "Bye", "hello my friend,hello")
    print(ret)
    ret = re.sub(r"\d+", add, "python = 100,cpp = 99")
    print(ret)


def tool():
    # print("a" == "" "a")
    # r = re.match("r(\d*)", "a")
    r = re.match("(\d*)", "a")
    print(r.group(1))  # 输出这一行的结果是一个空字符串


if __name__ == '__main__':
    # match_main()
    # print("-" * 90)
    # search_findall_main()
    # print("-"*90)
    # tool()
    # print("-" * 90)
    sub_main()
