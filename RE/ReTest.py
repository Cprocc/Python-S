import re

# test1
s = """
http://www.interoem.com/messageinfo.asp?id=35
http://3995503.com/class/class09/news_show.asp?id=14
http://lib.wzmc.edu.cn/news/onews.asp?id=769
http://www.zy-ls.com/alfx.asp?newsid=377&id=6
http://www.fincm.com/newslist.asp?id=415
"""
res = re.findall(r"http://.+?com|http://.+?cn", s)
for i in range(len(res)):
    print(res[i])

# test2
s1 = "hello world ha ha"
res = (re.split("\W+", s1))
for i in range(len(res)):
    print(res[i])
