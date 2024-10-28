# 把地址取名叫做url url就代表了这个地址！
url = 'https://m803.music.126.net/20240131125305/b10fa09005cac0aaee5e3bec1d22276a/jd-musicrep-privatecloud-audio-public/obj/woHCgMKXw6XCmDjDj8Oj/23865219535/1909/202309143234/781c1731c92a4b8044d8532ab1e49eac.mp3'

# 加载 requests网络模块包 网络功能模块！！
import requests

# 使用网络请求语法 请求地址
r = requests.get(url)   # r就是请求的行为

# 请求地址后 得到结果里的 二进制数据！  .content
g = r.content   # g就是接收了 请求地址后 的 二进制数据资源！

w = open('audio.mp3','wb')
w.write(g)

