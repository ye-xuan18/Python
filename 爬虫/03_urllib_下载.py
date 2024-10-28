# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 12:04 PM
# @Author : 叶轩
# @File : 03_urllib_下载
# @Project : 爬虫


import urllib.request

# 下载网页
# url_page = 'http://www.baidu.com'

# url代表的是下载的路径 filename文件的名字
# 在python中 可以写变量的名字 也可以直接写值
# urllib.request.urlretrieve(url_page, '百度.html')

# 下载图片
# url_image = 'https://pic3.zhimg.com/v2-c249b5987637b32ee67562dcb74ac4c8_r.jpg'
#
# urllib.request.urlretrieve(url=url_image, filename='华晨宇.png')

# 下载视频
url_video = 'https://v26-web.douyinvod.com/855d100e4f79cbdeae41a262749dedab/65d82aba/video/tos/cn/tos-cn-ve-15/oonafAUEleAE3DQuBX8DgOnXA1A9SnjRggbTNz/?a=6383&ch=10010&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=458&bt=458&cs=2&ds=6&ft=bvTKJbQQqUuSfmE0mo0OqY8hFgpiwS2sejKJVs4voG0P3-I&mime_type=video_mp4&qs=11&rc=NmdlaGVlNmRlNTZoaDZoOkBpampqNTg6ZjhtcTMzNGkzM0BiMGIxLV5jX2MxYy42NGFfYSNsNmJwcjRvNF9gLS1kLWFzcw%3D%3D&btag=e00028000&dy_q=1708661839&feature_id=c6de0308cacfd993ef282c8e1c646267&l=2024022312171815384B1E9F29767F100B'
urllib.request.urlretrieve(url_video, '男大学化妆.mp4')
