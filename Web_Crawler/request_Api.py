import requests
url = 'http://cdn.heweather.com/china-city-list.txt'
strhtml = requests.get(url)
strhtml.encoding= 'utf8'
data = strhtml.text

for i in range(6):
    data.remove(data[0])
for item in data:
    print(item[0:11])

# data1 = data.split('\r ')
# print(data1)
# for i in range(3):
#     data1.remove(data1[0])
# for item in data1:
#     print(item[0:11])