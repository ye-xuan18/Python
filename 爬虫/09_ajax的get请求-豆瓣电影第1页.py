# _*_ coding : utf-8 _*_
# @Time : 2024/2/24 12:50 PM
# @Author : 叶轩
# @File : 09_ajax的get请求-豆瓣电影第1页
# @Project : 爬虫


# get请求
# 获取豆瓣电影第一页的数据  并且保存下来

import urllib.request

url = 'https://movie.douban.com/j/chart/top_list?type=30&interval_id=100%3A90&action=&start=0&limit=20'

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# （1）请求对象的定制
request = urllib.request.Request(url=url, headers=headers)

# （2）获取响应的数据
response = urllib.request.urlopen(request)
content = response.read().decode('utf-8')

# （3）数据下载到本地
# fp = open('douban.json', 'w', encoding='utf-8')
# fp.write(content)

with open('douban1.json', 'w', encoding='utf-8') as fp:
    fp.write(content)
