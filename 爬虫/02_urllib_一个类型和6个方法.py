# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 11:46 AM
# @Author : 叶轩
# @File : 02_urllib_一个类型和6个方法
# @Project : 爬虫

import urllib.request

url = 'http://www.baidu.com'

# 要模拟浏览器向服务器发送请求
response = urllib.request.urlopen(url)

# 一个类型和6个方法
# response是HTTPResponse的类型
# print(type(response))

# 按照一字节一字节的去读
# content = response.read()
# print(content)

# 返回多少个字节
# content = response.read(5)
# print(content)

# 读取一行
# content = response.readline()
# print(content)

# 多行读取
# content = response.readlines()
# print(content)

# 返回状态码  如果是200了  那么就证明我们的逻辑没有错
# print(response.getcode())

# 返回url地址
# print(response.geturl())


# 获取的是一些状态信息
# print(response.getheaders())

# 一个类型HTTPResponse
# 六个方法 read  readline  readlines   getcode geturl getheaders
