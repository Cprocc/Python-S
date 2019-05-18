import requests
import pymongo
import json

client = pymongo.MongoClient('localhost', 27017)
#新建数据库
taobao = client['taobao']
#新建表
search_result = taobao['search_result']

#爬取淘宝某电商平台数据

url = 'https://s.taobao.com/search?q=%E8%BF%9E%E8%A1%A3%E8%A3%99&search=%E6%8F%90%E4%BA%A4&tab=all&sst=1&n=20&buyitnow&m=api4h5&abtest=24&wlsort=24&page=1'
strhtml = requests.get(url)
result = strhtml.json()

for item in result['listItem']:
    json_data = {
        'title' : item['title'],
        'price' : float(item['price']),
        'sold' : int(item['sold']),
        'location' : item['location']
    }
