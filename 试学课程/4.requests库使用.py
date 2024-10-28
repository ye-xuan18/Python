# 1.安装 -- pip install requests

# 2.基本使用 --百度

import requests   # 引入库文件

# 找到目标url

# url = 'http://www.baidu.com'

# 发送请求

# responce = requests.get(url)
# print(responce)        # <Response [200]>  200是状态码

# 打印响应
# print(responce.status_code)    # 状态码
# print(responce.reason)        # 状态码的解释
# print(responce.url)           # 响应的url
# print(responce.headers)       # 响应的头部信息
# print(responce.encoding)      # 响应的编码方式
# 将其编码设置为UTF-8

# responce.encoding = 'utf-8'
# print(responce.text)    # 响应内容有乱码，requests模块会自动寻找一种解码方式去解码
# print(responce.content.decode())
# print(len(responce.content))
# 3.使用requests库保存图片

# 确定url

# url = 'https://img2.baidu.com/it/u=3258571338,2779685785&fm=253&fmt=auto&app=138&f=JPEG?w=800&h=500'

# 发送请求，获取响应

# res = requests.get(url)
# print(res.content)    打印内容

# 保存响应

# with open('百度图片.jpg', 'wb') as f:
#     f.write(res.content)

# 4.其他属性

# responce.text 和 responce.content的区别：
# text ：str类型： requests模块自动根据http头部对响应的编码有根据的推测
# content：byte类型， 可以通过decode(解码)

# 5.用户代理

# 百度首页代码爬取到的比较少
# 请求头中user-agent字段必不可少，表示客户端的操作系统以及浏览器的信息

url = 'http://www.baidu.com'

# 构建请求头
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}
# 带上user-agent发送请求
# 发送请求
# headers接收字典形式的请求头，请求头字段名为key，值为value

response = requests.get(url,headers=headers)
print(response.content.decode())  # 打印源码
print(len(response.content.decode()))  # 打印长度

# 添加user-agent的目的是为了让服务器认为是浏览器在发送请求，而不是爬虫程序在发送请求
