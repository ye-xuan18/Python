# _*_ coding : utf-8 _*_
# @Time : 2024/2/29 7:03 PM
# @Author : 叶轩
# @File : 05_运算符
# @Project : 千锋教育


"""
运算符
赋值运算符
"""

# 算数运算符 :  + - * / % // **

a = 1
b = 2

c = a + b

# print(a, b, c, 1000, 10000, sep='#')
# print(a, b, c, end='\n')  # 1 2 3  表示末尾不换行
print(a, b, c)

print(c - a)

print(c * a)

print(c / 2)  # 除法

print(c // 2)  # 整除

print(2 ** 3)  # m ** n  表示是m的n次方

#   取模  取余
print(3 % 2)  # 奇数  偶数

'''
键盘输入一个3位数的整数，打印个位数、十位数、百位数
'''

# number = int(input('请输入一个三位整数:'))
# number = int(number)

number = int(input('请输入一个三位整数:'))
print('个位数:', number % 10)
print('十位数:', number // 10 % 10)
print('百位数:', number // 100)
