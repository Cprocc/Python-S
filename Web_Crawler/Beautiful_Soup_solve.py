# 获取cntour.cn网站上的所有标题
import  requests
import re
from bs4 import BeautifulSoup
url = 'http://www.cntour.cn/'
strhtml = requests.get(url)
soup = BeautifulSoup(strhtml.text, 'lxml')
data = soup.select('#main > div > div.mtop.firstMod.clearfix > div.centerBox > ul.newsList > li > a ')
print(data)
for item in data:
    result = {
        'title' : item.get_text(),
        'link' : item.get('href'),
    #     匹配每一篇文章链接前面的数字ID
        'ID' : re.findall('\d+',item.get('href'))
    }
    print(result)