# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 1:04 PM
# @Author : 叶轩
# @File : 32_字典的高级_查询
# @Project : Python基础


# 定义一个字典

person = {'name': '韩東', 'age': 24, 'height': '193cm'}

# 访问person的name
# print(person['height'])
# print(person['name'])

# 使用[]的方式获取字典中不存在的key的时候  会发生异常 keyerror
# print(person['sex'])

# 不能使用.的方式来访问字典的数据
# print(person.name)


# print(person.get('height'))
# print(person.get('name'))
# print(person.get('age'))


# 使用.的方式  获取字典中不存在的key的时候  会返回None值
print(person.get('sex'))
