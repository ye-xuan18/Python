# _*_ coding : utf-8 _*_
# @Time : 2024/2/29 6:15 PM
# @Author : 叶轩
# @File : 04_类型转换练习
# @Project : 千锋教育

"""
键盘输入两个数，输出两个整数的和，输出差
input('请输入一个数:')
input('请输入第二个数:')
"""

one = input('输入一个数:')
two = input('输入第二个数:')

# 进行计算
print(one + two)

# 转换
print(int(one) + int(two))

print(float(one) + float(two))

# 差
print(int(one) - int(two))

print(float(one) - float(two))

a = 9.49
print(int(a))


'''
以变量名a:
str ===> int  int(a)  但是如果'9.9'而且是字符串类型转成int就会报错了
str ===> float float(a)
int ===> str
float ===> str
int ===> float  float(a)
float ===> int  int(a)  只不过float类型中小数点后面的数字被抹掉了
'''

flag = True
print(int(flag))
flag = False
print(int(flag))
print(float(flag))
print(str(flag))

a = 5
print(bool(a))
a = 0
print(bool(a))

a = ''
print(bool(a))

# 当变量是0或者空字符串的时候，转换结果是False，只要变量有值则为True
