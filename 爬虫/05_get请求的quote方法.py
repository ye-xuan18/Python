# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 3:18 PM
# @Author : 叶轩
# @File : 05_get请求的quote方法
# @Project : 爬虫

# https://www.baidu.com/s?wd=%E5%8D%8E%E6%99%A8%E5%AE%87


# 需求   获取https://www.baidu.com/s?wd=华晨宇的网页源码


import urllib.request

url = 'https://www.baidu.com/s?wd='

# 请求对象的定制是为了解决反爬的第一种手段

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 要将华晨宇三个字变成unicode编码的格式
# 我们要依赖urllib.parse

name = urllib.parse.quote('华晨宇')

url = url + name
print(url)
# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
request = urllib.request.urlopen(request)

# 获取响应的内容
content = request.read().decode('utf-8')

# 打印数据
print(content)
