# 引入库文件
import requests

# 找到目标url
url = 'https://pvp.qq.com/'

# 构建请求头信息
headers={
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36'
}

# 发送请求获取响应
res = requests.get(url, headers=headers)

# 设置编码格式
res.encoding = 'gbk'

print(res.content)

# 保存文件
with open ('王者荣耀源代码.html','wb')  as f:
    f.write(res.content)



