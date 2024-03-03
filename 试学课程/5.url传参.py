# user-agent池 --防止反爬
# 随机调用
# 第一种
# import random
# UAlist = [
#     'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
#     'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1'
#     'Mozilla/5.0 (Linux; Android 9.0; SAMSUNG SM-F900U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
# ]
# print(random.choice(UAlist))


# 第二种
from fake_useragent import UserAgent  # 可能会出现异常
# print(UserAgent().random)

# 2.浏览器发送请求原理
# 1.构建请求
# 2.查找缓存
# 3.准备ip地址和端口
# 4.等待tcp队列队列
# 5.建立tcp连接
# 6.发送http请求

# 浏览器会向服务器发送请求，包括了请求方法，请求url，http协议# https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=1&rsv_idx=1&tn=baidu&wd=%E5%AD%A6%E4%B9%A0&fenlei=256
# https://cn.bing.com/search?q=%E5%A4%A7%E6%95%B0%E6%8D%AE&PC=U316

# 字符串被当做url提交时会被自动进行url编码处理

# 输入  ---大数据
# 发送请求的时候   --- E5%A4%A7%E6%95%B0%E6%8D%AE  密文

# from urllib.parse import quote,unquote
# quote()   #明文转密文    传参数类型：字符串
# unquote() #密文转明文    传参数类型：%x%x%x

# print(quote('参数'))   # %E5%8F%82%E6%95%B0
# print(unquote('%E5%8F%82%E6%95%B0')) # 参数
# wd=参数
# https://cn.bing.com/search?q=%E5%A4%A7%E6%95%B0%E6%8D%AE


# 4.发送带参数的请求
import requests
# url='https://www.baidu.com/s?wd=%E5%AD%A6%E4%B9%A0'
#
# headers={
#     'User-Agent':'Mozilla/5.0 (Linux; Android 9.0; SAMSUNG SM-F900U Build/PPR1.180610.011) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Mobile Safari/537.36'
# }
# res=requests.get(url,headers=headers)
# print(res.content.decode())

# 通过params携带参数字典
# 1.构建请求参数字典
# 2.发送请求的时候带上请求参数字典

url = 'https://www.baidu.com/s?'

headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 构建请求参数字典
name = input('请输入想要输入的关键字:')
kw = {'wd': 'name'}

res2 = requests.get(url, headers=headers, params=kw)
print(res2.content.decode())