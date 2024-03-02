# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 7:41 PM
# @Author : 叶轩
# @File : 41_文件的打开和关闭
# @Project : Python基础

# 创建一个test.txt文件
# open(文件的路径)
# 模式:  w   可写
#       r   可读
# open('test.txt', 'w')

# 打开文件
# fp = open('test.txt', 'w')
# fp.write('HanDong')

# 文件夹是不可以创建的 暂时需要手动创建
# fp = open('demo/test.html', 'w')
# fp.write('hello Handong')

# 文件的关闭
fp = open('a.txt', 'w')
fp.write('hello')
fp.close()
