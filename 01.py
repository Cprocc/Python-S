# 01直接获取
"""import requests
url='https://www.zhihu.com/question/20399991'
r = requests.get(url)
text= r.text

text """

#02 （因为python默认的头部被识别）伪装头部后获取
# 跑出一堆URL我的电脑要卡死了
"""import requests
header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36'}
url='https://www.zhihu.com/question/20399991'
r = requests.get(url,headers=header)
text= r.text

text 

#03  得到一堆url后，正则选出是图片的
import re
jpg = re.compile(r'https://[^\s]*?\.jpg')
jpeg = re.compile(r'https://[^\s]*?\.jpeg')
gif = re.compile(r'https://[^\s]*?\.gif')
png = re.compile(r'https://[^\s]*?\.png')
imgs=[]
imgs+=jpg.findall(text)
imgs+=jpeg.findall(text)
imgs+=gif.findall(text)
imgs+=png.findall(text)

#04 下载
def download(url):
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False


#05  
errors = []
for img_url in imgs:
    if download(img_url):
        print("download :"+img_url)
    else:
        errors.append(img_url)
#后两行错误提示运行有语法问题未解决
#print("ERROR URLS:")
#print(errors)"""

#final
import os
import re
import requests
def download(folder,url):
    if not os.path.exists(folder):
        os.makedirs(folder)
    req = requests.get(url)
    if req.status_code == requests.codes.ok:
        name = url.split('/')[-1]
        f = open("./"+folder+'/'+name,'wb')
        f.write(req.content)
        f.close()
        return True
    else:
        return False

header = {'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

errs=[]

def fetch(url):
    r = requests.get(url,headers=header)
    text= r.text
    imgs=[]
    jpg = re.compile(r'https://[^\s]*?_r\.jpg')
    jpeg = re.compile(r'https://[^\s]*?_r\.jpeg')
    gif = re.compile(r'https://[^\s]*?_r\.gif')
    png = re.compile(r'https://[^\s]*?_r\.png')

    imgs+=jpg.findall(text)
    imgs+=jpeg.findall(text)
    imgs+=gif.findall(text)
    imgs+=png.findall(text)


    errors = []

    folder = url.split('/')[-1]
    for img_url in imgs:
        if download(folder,img_url):
            print("download :"+img_url)
        else:
            errors.append(img_url)
    return errors

urls=['https://www.zhihu.com/question/33304970',
       'https://www.zhihu.com/question/28853910']
for url in urls :
    print(url)
    errs+=fetch(url)

print("ERROR URLS:")
print(errs)
