# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 4:08 PM
# @Author : 叶轩
# @File : 07_post请求百度翻译
# @Project : 爬虫

# post请求

import urllib.request
import urllib.parse

url = 'https://fanyi.baidu.com/sug'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

data = {
    'kw': 'spider'
}

# Post的请求的参数  必须要进行编码
data = urllib.parse.urlencode(data).encode('utf-8')
print(data)

# post的请求参数  是不会拼接在url的后面的  而是需要放在请求对象的参数中
# post请求的参数  必须要进行编码
request = urllib.request.Request(url=url, data=data, headers=headers)

# 模拟浏览器 向服务器发送请求
response = urllib.request.urlopen(request)

# 获取响应的数据
content = response.read().decode("utf-8")

# 字符串--》json对象

import json

obj = json.loads(content)
print(obj)

# 打印数据
print(content)

# post请求方式的参数 必须编码 data = urllib.request.urlencode(data).encode("utf-8")
# 编码之后必须调用encode方法
# 参数是放在请求对象定制的方法中 request = urllib.request.Request(url=url,data=data,headers=headers)
