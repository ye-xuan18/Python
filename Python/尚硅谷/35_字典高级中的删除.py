# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 1:25 PM
# @Author : 叶轩
# @File : 35_字典高级中的删除
# @Project : Python基础

# del
# （1） 删除字典中指定的某一个元素
person = {'name': '韩東', 'age': 24, 'height': '193cm'}

# # 删除之前
# print(person)
#
# del person['age']
#
# # 删除之后
# print(person)

# （2） 删除整个字典
# 删除之前
# print(person)
#
# del person
#
# # 删除之后
# print(person)


# clear
# （3） 清空字典 但是保留字典对象

print(person)
# 清空指的是将字典中所有的数据  都删除掉 而保留对象
person.clear()

print(person)
