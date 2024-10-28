# _*_ coding : utf-8 _*_
# @Time : 2024/2/28 5:40 PM
# @Author : 叶轩
# @File : 01_变量
# @Project : 千锋教育

"""
变量："容器"
弱语言：变量声明的时候对数据类型不是很严格
java： int a = 100     float b = 9.9
python的特点:a = 100
1、怎么起名
2、可以赋什么值
3、有哪些数据类型

变量名的起名规范
1、字母、数字、下划线，其他的特殊符号不可以包括（$)
2、不能用数字开头
3、不能使用关键字
4、区分大小写
"""

name = 'yexuan'
age = 19

A = 100
a = 200

print(type(A))
print(type(a))
print(type(name))
print(type(age))

# 见名知义：getnamebyline
# getNameByLine  驼峰式：开头第一个单词全部小写，小驼峰

getNameByLine = 'hello'
get_name_by_line = 'hello'

# 大驼峰：python 面向对象：类名：每个单词的首字母全部大写

名字 = 'yexuan'
print(名字)