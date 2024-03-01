# _*_ coding : utf-8 _*_
# @Time : 2024/2/28 6:10 PM
# @Author : 叶轩
# @File : 02_数据类型
# @Project : 千锋教育

"""
数据类型
int
float
string
boolean
"""

money = 10000000  # 声明一个名称为money的变量，赋值为10000000
print(type(money))  # int:整形
# print()是一个内置函数，负责输出结果

# money 是一个变量，后面的值允许发生变化。

money = 3.141592653  # float: 浮点型
print(type(money))

money = '10000000000000000000'  # str：字符串类型
print(type(money))
money = "10000000000000000000"  # str：字符串类型
print(type(money))
money = '''10000000000000000000'''  # str：字符串类型
print(type(money))

message = '叶轩说:"今天天气很不错"'
print(message)
print(type(message))
message = "叶轩说:'今天天气很不错'"
print(message)
print(type(message))

ancient =\
    '''
          静夜思
          李白
    床前明月光，疑是地上霜。
    举头望明月，低头思故乡。
'''

print(ancient)
print(type(ancient))


# 布尔类型  True、False 它俩是关键字
# 开发中判断：比如：是否登录成功，........
Login = True   # 真
print(Login)
print(type(Login))

Login = False  # 假
print(Login)
print(type(Login))
