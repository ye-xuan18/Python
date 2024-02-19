import requests

content = input('请输入您要搜索的内容')
url = f'https://www.sogou.com/web?query={content}'
headers = {
    # 添加一个请求头信息.UA
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
}
# 处理一个小小的反爬
resp = requests.get(url,headers=headers)
print(resp.text)

