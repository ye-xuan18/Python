url = 'https://v3-weba.douyinvod.com/deb7169b902f4ac2bdf78743372c3fff/65b9e641/video/tos/cn/tos-cn-ve-15c001-alinc2/oYYxP6g2tAIiLm6OQzeyISB7GhACfAtqXIJEmM/?a=6383&ch=26&cr=3&dr=0&lr=all&cd=0%7C0%7C0%7C3&cv=1&br=706&bt=706&cs=2&ds=3&ft=XzJ6BM06xxouCA.D42D12lop0BanGbvibGkwF_79T.jQ2Nz7T&mime_type=video_mp4&qs=15&rc=PDdkZGRnaGVmODM5Zmk6aUBpanQ1bGY6ZjprcDMzNGkzM0AuMjZeYTVfXi0xNWM2LzIyYSNxaTBfcjRvM2xgLS1kLS9zcw%3D%3D&btag=e00028000&dy_q=1706678209&feature_id=8129a1729e50e93a9e951d2e5fa96ae4&l=20240131131648C950ADC3745F4C0A3DC7'

import requests

g = requests.get(url)

r = g.content

d = open('宁崽语录.mp4','wb')
d.write(r)
