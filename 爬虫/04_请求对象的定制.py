# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 12:32 PM
# @Author : 叶轩
# @File : 04_请求对象的定制
# @Project : 爬虫


import urllib.request

url = 'https://www.baidu.com'

# url的组成
# https://cn.bing.com/search?q=%E5%8D%8E%E6%99%A8%E5%AE%87&PC=U316&FORM=CHROMN
# http/https  cn.bing.com       80/443    search   wd = '华晨宇'     #
#     协议        主机            端口号      路径        参数         锚点
# http 80
# http 443
# mysql 3306
# oracle 1521
# redis 3306
# mongodb 27017

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 因为urlopen方法中不能存储字典 所以headers不能传递进去
# 请求对象的定制
# 注意  因为参数顺序的问题  不能直接写url 和 headers 中间还有data  所以我们需要关键字传参
request = urllib.request.Request(url=url, headers=headers)

response = urllib.request.urlopen(request)

content = response.read().decode('utf-8')

print(content)
