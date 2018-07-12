# 以get方式抓取数据
import requests
import time

url = 'http://www.cntour.cn/'
time.sleep(3)
# proxies = {
#     "http" : "http://10.10.1.10:3128",
#     "https" : "http://10/10.1.10:1080"
#     }
# response = requests.get(url, proxies = proxies)
# print(response.text)

headers = {'User-Agent' :'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 '
                         '(KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36' }
strhtml = requests.get(url,headers = headers)
print(strhtml.text)

