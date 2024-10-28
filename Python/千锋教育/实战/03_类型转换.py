# _*_ coding : utf-8 _*_
# @Time : 2024/2/29 1:49 PM
# @Author : 叶轩
# @File : 03_类型转换
# @Project : 千锋教育


print('你好,叶轩')
name = '叶轩'
print(name)

# input

username = input('请输入用户名:')   # 阻塞
print('哈哈哈')
print(username)
print(type(username))

money = input("请输入您的缴费金额:")
print(money)
print(type(money))
print(int(money) + 1000)