# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 7:22 PM
# @Author : 叶轩
# @File : 39_函数的返回值
# @Project : Python基础


# 返回值的关键字是return ，存在函数中
def qmodel():
    return '韩東'


# 使用一个变量来接受函数的返回值
model = qmodel()
print(model)


# 案例练习
# 定义一个函数 让函数计算两个数值 并且返回这个计算之后的结果
def sum(x, y):
    z = x + y
    return z


q = sum(110, 520)
print(q)
