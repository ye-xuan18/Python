import requests

url = 'https://movie.douban.com/j/chart/top_list'

data = {
'type': '30',
'interval_id': '100:90',
'action':'',
'start': '0',
'limit': '20'
}

headers = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
}
resp = requests.get(url,params=data,headers=headers)
print(resp.text)
# print(resp.json())
# print(resp.url)
