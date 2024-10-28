# _*_ coding : utf-8 _*_
# @Time : 2024/3/2 11:51 AM
# @Author : 叶轩
# @File : 08_逻辑运算符
# @Project : 千锋教育

"""
逻辑运算符：and    or   not

结果：
and：  与    而且
A  and  B
True  and  True     ===>True
True  and  False   ===>False
False and  True     ===>False
False and  False    ===>False



or  : 或   或者    只要有一侧为真True  结果即为True

A or B
True  or  True     ===>True
True  or  False   ===>True
False or  True     ===>True
False or  False    ===>False

not ：
not True ===>False
not False ===>True

"""
a = 1
b = 3

print(a and b)  # and两边都是非0的数字，结果是最后面的数字值

c = 0
print(c and a)  # and两边只要有一侧为0，结果即为0

print(c < a < b)  # username  == 'yexuan' and password == '1111111'
print(a == c and a < b)

print('*' * 20)  # 打印20个*
print('#' * 20)  # 打印20个#
print('-' * 20)  # 打印20个-

print(b or a)
print(a or b)

print(c or b)
print(a > c or a < b)
print(a == c or a < b)  # 场景：1、账号密码 or  2、手机号码  验证码
# 账号名/手机号码 + 密码

flag = True
print(not flag)

print(not (a > c))
