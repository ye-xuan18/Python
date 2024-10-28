# _*_ coding : utf-8 _*_
# @Time : 2024/2/20 3:21 PM
# @Author : 叶轩
# @File : 05_查看变量的数据类型
# @Project : Python基础


# int
# float
# boolean
# string
# list
# tuple
# dict
# type方法判断变量的数据类型
# 格式：type(变量)





# int
a = 1
print(a)
print(type(a))

# float
b = 1.2
print(b)
print(type(b))

# boolean
c = True
print(c)
# <class 'bool'>
print(type(c))

# string
d = '韩東是一个穿搭博主也是一个模特,真的又酷又帅又高'
print(d)
# <class 'str'>
print(type(d))

# list
e =[1,2,3,4]
print(e)
# <class 'list'>
print(type(e))

# tuple
f = (1,2,3,4,5)
print(f)
# <class 'tuple'>
print(type(f))

# dict
g = {'name':'华晨宇','age':18}
print(g)
print(type(g))