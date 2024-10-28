# 把地址取名叫做url url就代表了这个地址！
url = 'https://img1.baidu.com/it/u=273192805,2639459452&fm=253&fmt=auto&app=120&f=JPEG?w=500&h=889'

# 加载 requests网络模块包 网络功能模块！！
import requests

# .get()请求语法！ 会请求括号里面的值
g = requests.get(url)   #请求地址的操作我们存给了g 接收了

# 如果请求后需要得到2进制数据  需要写 .content
r = g.content  # r 接收了请求地址后 的 二进制数据啦！ （图片、数据、视频）

# 创建文件  专门用于打开这个 数据！
# web就是如果文件不存在 则生成 二进制空文件
d = open('华晨宇.jpg','wb')  # d就是代表了这个空文件
d.write(r)  # 往d 中写入数据




