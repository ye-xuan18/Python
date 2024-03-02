# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 1:34 PM
# @Author : 叶轩
# @File : 36_字典高级_遍历
# @Project : Python基础

# 遍历 -- 就是数据一个一个的输出
person = {'name': '韩東', 'age': 24, 'height': '193cm', 'sex': '男'}

# （1） 遍历字典的key
# 字典.keys(）方法 获取的字典中所有的key值  key是一个变量的名字  我们可以随便起
# for key in person.keys():
#     print(key)

# （2） 遍历字典的value
# 字典.values() 方法  获取字典中所有的value值 value也是一个变量 我们可以随便命名
# for value in person.values():
#     print(value)

# （3） 遍历字典的key和value
# for key, value in person.items():
#     print(key, value)

# （4） 遍历字典的项/元素
for item in person.items():
    print(item)
