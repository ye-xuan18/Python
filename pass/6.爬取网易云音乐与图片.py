# 引入requests库

import requests

# 1.获取单张图片
# 找到目标url
# url = 'https://p1.music.126.net/6rMD39V8q3OEj8oW0TsEkg==/109951169306583696.jpg?imageView&quality=89'

# # 构建请求头字典
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
# }

# # 发送请求，获取响应
# img = requests.get(url,headers=headers)
# # print(img.content)  二进制数据

# # 保存图片
# with open('网易云图片.jpg','wb') as f:
#     f.write(img.content)

# 2.获取单首歌曲
# url ='https://m803.music.126.net/20240203120813/163cbca7c84242087aa5a12fa32f0c52/jd-musicrep-privatecloud-audio-public/obj/woHCgMKXw6XCmDjDj8Oj/23394831256/500e/20221120143029/964e487b10e231af8aebb7c636da2f8f.mp3'
# music = requests.get(audio)
# # print(music.content)
# with open('小镇里的花.MP3','wb') as f:
#     f.write(music.content)


# 3.获取单个mv
# url = 'https://vodkgeyttp8.vod.126.net/cloudmusic/obj/core/25559024708/5c46fedcf0bf64cfed2fbcff6ed9a9fb.mp4?wsSecret=77443a2565c9acfb8b63fac76f5aa961&wsTime=1706933794'
# video = requests.get(url)
# # print(video.content)
# with open('小镇里的花.mp4','wb') as f:
#     f.write(video.content)

# 4.百度贴吧单页获取案例
# url = 'https://tieba.baidu.com/f?ie=utf-8&kw=%E5%8D%8E%E6%99%A8%E5%AE%87&fr=search'
# headers ={
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
# }
# responce = requests.get(url,headers=headers)
# print(responce.text)
# with open('华晨宇.html','wb') as f:
#     f.write(responce.content)

# 5.百度贴吧多页获取案例
# https://tieba.baidu.com/f?kw=%E5%8D%8E%E6%99%A8%E5%AE%87&ie=utf-8&pn=0
# https://tieba.baidu.com/f?kw=%E5%8D%8E%E6%99%A8%E5%AE%87&ie=utf-8&pn=50
# https://tieba.baidu.com/f?kw=%E5%8D%8E%E6%99%A8%E5%AE%87&ie=utf-8&pn=100
# https://tieba.baidu.com/f?kw=%E5%8D%8E%E6%99%A8%E5%AE%87&ie=utf-8&pn=150

# 规律：
# pn: 第一页0  第二页50  第三页100  第四页150

# for i in range(4):
#     print(i * 50)

# url = 'https://tieba.baidu.com/f?'
#
# headers = {
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0'
# }
#
# word = input('请输入您的贴吧名字:')
#
# page = int(input('亲输入要保存的页数:'))
#
# for i in range(page):
#     params = {
#         'kw': word,
#         'pn': i * 50
#     }
#
#     # 发送请求
#     responce = requests.get(url,headers=headers,params=params)
#
#     # 保存数据.html
#     with open(f'{word}{i+1}.html','wb') as f :
#         f.write(responce.content)

