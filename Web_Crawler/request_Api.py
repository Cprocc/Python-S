import requests
url = 'http://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
strhtml.encoding= 'utf8'
data = strhtml.text
data1 = data.split( ' ')
print (data1)
for i in range(5):
    data1.remove(data1[0])
for item in data1:
    print(item[0:11])