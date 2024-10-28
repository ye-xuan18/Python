# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 3:49 PM
# @Author : 叶轩
# @File : 06_get请求的urlencode方法
# @Project : 爬虫


# urlencode应用场景 ：多个参数的时候

# https://www.baidu.com/s?wd=华晨宇&sex=男

# import urllib.parse
#
# data = {
#     'wd': '华晨宇',
#     'sex': '男',
#     'location': '湖北武汉'
# }
# a = urllib.parse.urlencode(data)
# print(a)
# 获取https://www.baidu.com/s?wd=%E5%8D%8E%E6%99%A8%E5%AE%87&sex=%E7%94%B7的网页源码

import urllib.parse
import urllib.request

base_url = 'https://www.baidu.com/s?'

data = {
    'wd': '华晨宇',
    'sex': '男',
    'location': '湖北武汉'
}

new_data = urllib.parse.urlencode(data)
print(new_data)
# 请求资源路径
url = base_url + new_data

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# 模拟浏览器向服务器发送请求
response = urllib.request.urlopen(request)

# 获取网页源码数据
content = response.read().decode('utf-8')

# 打印数据
print(content)
