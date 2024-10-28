# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 1:17 PM
# @Author : 叶轩
# @File : 34_字典的高级_修改
# @Project : Python基础

person = {'name': '韩東', 'age': 24, 'height': '193cm'}
print(person)

# 给字典添加一个新的key value
# 如果使用变量名字['键'] = 数据时 这个键如果在字典中不存在  那么就会变成新增元素
person['profession'] = '服装表演生'
# 如果这个键在字典中存在 那么就会变成这个元素
person['height'] = '196cm'
print(person)
