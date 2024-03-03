# _*_ coding : utf-8 _*_
# @Time : 2024/3/2 11:25 AM
# @Author : 叶轩
# @File : 07_关系运算符
# @Project : 千锋教育

"""
关系运算符：  结果  True、False
> < >= <=  ==  !=

"""

a = 10
b = 25

print(a > b)  # False
print(a < b)  # True

print(a == b)  # False
print(a != b)  # True

x = 'abf'
y = 'abd'

print(x == y)  # False
print(x < y)  # False

c = 10
print(a >= 10)  # True

'''
输入考试分数，判断成绩是否在100到80之间？
'''

grades = float(input('请输入您的考试成绩:'))
print(80 <= grades <= 100)
'''
输入iPhone 15Pro Max手机的价格：
输入HUAWEI mate40 的价格：
判断是否价格相同
'''
Aprice = int(input('请输入苹果手机的价格:'))
Hprice = int(input('请输入华为手机的价格:'))
print(Aprice == Hprice)
