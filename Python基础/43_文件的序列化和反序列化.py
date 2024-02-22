# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 8:17 PM
# @Author : 叶轩
# @File : 43_文件的序列化和反序列化
# @Project : Python基础
# fp = open('test.txt', 'w')
# 默认情况下我们只能把字符串写入文件中
# fp.write('hello World\n' * 10)
#
# fp.close()
#
# fp = open('test.txt', 'w')
# # 默认情况下 对象是无法写入文件中的 如果想写入 必须使用序列化操作
# name_list = ['wangxianyi', 'handong']
# fp.write(name_list)

# 序列化的两种方式
# dumps()
# (1)创建一个文件
# fp = open('test.txt', 'w')

# 定义一个列表
# name_list = ['handong', 'wangxianyi', 'jiangjiale']

# 导入json模块到该文件中
import json

# 序列化
# 将python对象  变成  json字符串
# 我们在使用scrapy框架的时候 该框架会返回一个对象  我们要将对象写入到文件中 就要使用json.jumps
# names = json.dumps(name_list)
# # 将names写入到文件中
# fp.write(names)
# fp.close()


# dump
# 再将对象转换为字符串的同时，指定一个文件的对象 然后把转换后的字符串写入到这个文件里

# fp = open('text.txt', 'w')
#
# name_list = ["handong", "wangxianyi", "jiangjiale"]
#
# import json
#
# json.dump(name_list, fp)
#
# fp.close()

# 反序列化
# # 将json的字符串变成一个python对象
# fp = open("text.txt", "r")
# content = fp.read()
# # print(content)
# # print(type(content))
#
# # loads
# import json
#
# # 将字符串变成python对象
# result = json.loads(content)
# print(result)
# print(type(result))


# load

# fp = open("text.txt", "r")
#
# import json
#
# result = json.load(fp)
#
# print(result)
# print(type(result))
# fp.close()
