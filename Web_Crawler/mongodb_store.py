import requests
import time
import pymongo

client = pymongo.MongoClient('localhost', 27017)
book_weather = client['weather']
sheet_weather = book_weather['sheet_weather_3']

url = 'http://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
data = strhtml.text
data1 = data.split("\r ")
for i in range(3):
    data1.remove(data1[0])
for item in data1:
    url = 'https://free-api.heweather.com/v5/forecast?city=' + item[0:11] +' &key = 7d0daf2a85f64736a42261161cd3060b '
    strhtml = requests.get(url)
    strhtml.encoding = 'utf8'
    time.sleep(1)
    dic = strhtml.json()
    sheet_weather.insert_one(dic)