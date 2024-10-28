url = 'https://aod.cos.tx.xmcdn.com/storages/cf77-audiofreehighqps/2A/B0/GKwRIW4IUXvmACgVqQIlDJ_v.m4a'
import requests
a = requests.get(url)
b = a.content
d = open('摸金校尉.mp3','wb')
d.write(b)