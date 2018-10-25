import re
s = """
<div>
        <p>岗位职责：</p>
<p>完成推荐算法、数据统计、接口、后台等服务器端相关工作</p>
<p><br></p>
<p>必备要求：</p>
<p>良好的自我驱动力和职业素养，工作积极主动、结果导向</p>
<p>&nbsp;<br></p>
<p>技术要求：</p>
<p>1、一年以上 Python 开发经验，掌握面向对象分析和设计，了解设计模式</p>
<p>2、掌握HTTP协议，熟悉MVC、MVVM等概念以及相关WEB开发框架</p>
<p>3、掌握关系数据库开发设计，掌握 SQL，熟练使用 MySQL/PostgreSQL 中的一种<br></p>
<p>4、掌握NoSQL、MQ，熟练使用对应技术解决方案</p>
<p>5、熟悉 Javascript/CSS/HTML5，JQuery、React、Vue.js</p>
<p>&nbsp;<br></p>
<p>加分项：</p>
<p>大数据，数理统计，机器学习，sklearn，高性能，大并发。</p>

        </div>

"""
# 匹配模式是贪婪的
s2 = "<h>>"
res = re.match(r"<(.+)>", s2)
print(res.group(1))
# 关闭贪婪,在，?+{m,n}后面加上?
s3 = "This number is 123-456-789-0"
r = re.match(r".+(\d+-\d+-\d+-\d+)", s3)
print(r.group(1))
r = re.match(r"(.+)(\d+-\d+-\d+-\d+)", s3)
print(r.group(1), r.group(2))
r = re.match(".+?(\d+-\d+-\d+-\d+)", s3)
print(r.group(1))

r = re.match(r"aaa(\d+?)ddd", "aaa2342ddd")
print(r.group(1))
print(re.match(r"aaa(\d+?)", "aaa2342").group(1))

# 替换掉<>
re.sub(r"<.+>", " ", s)
s = re.sub(r"</?\w+>", "", s)
# print(s)

# re.split()
# python2中常使用三个参数，中间的参数表示替换
# python3中一般有两个参数，如下的写法分割出字符串
s1 = "Info:Lily 33 American"
s1 = re.split(r"\W+", s1)
# print(s1)
