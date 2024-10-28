# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 7:32 PM
# @Author : 叶轩
# @File : 40_函数的局部变量和全局变量
# @Project : Python基础


# 局部变量 :在函数的内部定义的变量  我们称为局部变量
# 特点：作用域范围是函数内部,而函数的外部是不可以使用的

# def f1():
#     # 在函数内部定义的变量 我们称做局部变量
#     a = 1
#     print(a)
#
#
# f1()
# print(a)


# 全局变量 ：定义在函数外部的变量 我们称之为全局变量
# 特点：可以在函数的外部使用，也可以在函数的内部使用

a = 1

print(a)


def f1():
    print(a)


f1()

# 在满足条件的情况下  要使用作用域最小的变量范围
