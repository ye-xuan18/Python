# 逻辑思考

# 百度贴吧图片下载

# 1.通过requests和lxml拿到网页源代码数据
# 2.通过lxml对源代码数据进行解析，拿到图片的url地址
# 3.依次对图片地址进行网络请求
# 4.把图片的原始内容写入图片文件

import requests
from lxml import etree

index_url = 'https://tieba.baidu.com/p/8861851603'

response = requests.get(index_url).text

selector = etree.HTML(response)

image_urls = selector.xpath('//img[@class="BDE_Image"]/@src')

offset = 0

for image_url in image_urls:

    image_content = requests.get(image_url).content

    with open('{}.jpg'.format(offset),'wb') as f:
        f.write(image_content)

    offset = offset+1


