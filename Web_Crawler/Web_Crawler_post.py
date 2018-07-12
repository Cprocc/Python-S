#使用POST方式抓取数据
import requests
import json

def get_translate_data(word = None):

    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
    # 实际做了改动，原URL是 http://fanyi.youdao.com/translate_o?smartresult=dict&smartresult=rule
    # url中？前有个_o，删除后，response中的errorCode=50就会解决。
    From_data = {
        'i':  word,
        'from':' AUTO',
        'to': 'AUTO',
        'smartresult':'dict',
        'client': 'fanyideskweb',
        'salt': '1531210679111',
        'sign': 'f6e7bfa353199fffbc5226acc7fad35e',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_CLICKBUTTION',
        'typoResult': 'false'
    }
    #请求表单数据
    response = requests.post(url, data = From_data)
    #将json格式转化为字符串
    content = json.loads(response.text)
    #打印翻译完的数据
    print(content['translateResult'] [0] [0] ['tgt'])
if __name__ == '__main__':
    get_translate_data('我爱国')