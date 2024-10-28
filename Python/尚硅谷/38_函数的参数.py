# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 7:08 PM
# @Author : 叶轩
# @File : 38_函数的参数
# @Project : Python基础


# 函数来计算1和2的和
# def sum():
#     a = 1
#     b = 2
#     c = a + b
#     print(c)
#
# sum()

def sum(a, b):
    c = a + b
    print(c)


# 位置参数    按照位置——对应的关系来传递参数
sum(1, 2)

sum(200, 300)

# 关键字传参
sum(a=200, b=300)

# 定义函数的时候 sum(a, b) 我们称a和b为形式参数  简称形参
# 调用函数的时候 sum(1, 2) 我们称1和2为实际参数  简称实参
