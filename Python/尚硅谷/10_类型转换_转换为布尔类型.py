# _*_ coding : utf-8 _*_
# @Time : 2024/2/20 6:54 PM
# @Author : 叶轩
# @File : 10_类型转换_转换为布尔类型
# @Project : Python基础


# 布尔类型转换为字符串
# 如果对非0的整数进行bool类型的转换 那么就全是true
# a = 1
# print(type(a))
# 将整形变成布尔类型的数据
# b = bool(a)
# print(b)
# print(type(b))


# a = 2
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = -1
# print(type(a))
#
# b = bool(a)
# print(b)
# print(type(b))

# a = 0
# print(type(a))
# # 在整数的范围内0强制类型转换为布尔类型的结果是false
# b = bool(a)
# print(b)
# print(type(b))

# 浮点数
# a = 1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
# a = -1.0
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# 字符串
# 只要字符串中有内容 那么在强制类型转换为bool的时候 那么就返回True
# a = '韩東是一个穿搭模特，身高193，拥有大长腿，衣服穿在他身上特别好看'
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = '   '
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# a = ''
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 列表
# 只要列表中有数据 那么强制类型转换为bool的时候 就返回True
# a = ['韩東','郑友韩', '张桐耀', '蒋家乐','刘俊熙','Ryan','张华','伊玖柒','王二博','李文宇', '刘骐豪','百夜']
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))
# 如果列表中什么数据都没有返回会的是false
# a = []
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# 元组
# 只要元组中有数据 那么强制类型转换为bool的时候 就会返回False
# a = ('韩東', '郑友韩', '张桐耀', '蒋家乐', '刘俊熙', 'Ryan', '张华', '伊玖柒', '王二博', '李文宇', '刘骐豪', '百夜')
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 字典
# 只要字典中有内容 那么在强制类型转换为bool的时候 就会返回True
# a = {'name': '韩東'}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))


# 如果在字典中没有数据的话 那么返回的就是False
# a = {}
# print(type(a))
# b = bool(a)
# print(b)
# print(type(b))

# 什么情况下是false
print(bool(0))
print(bool(0,0))
print(bool(''))
print(bool(""))
print(bool([]))
print(bool(()))
print(bool({}))


