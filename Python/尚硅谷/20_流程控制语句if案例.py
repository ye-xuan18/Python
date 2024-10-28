# _*_ coding : utf-8 _*_
# @Time : 2024/2/21 7:47 PM
# @Author : 叶轩
# @File : 20_流程控制语句if案例
# @Project : Python基础


#  在控制台上输入现在的身高 如果您13岁的身高大于180cm了 那么打印未来可以长到195以上
#  input返回的是字符串类型
height = input('请输入您现在13岁的身高:')

#  字符串和整数int是不能比较的
if int(height) > 180:
    print('未来可以长到195以上')

# 案例中考察了三个知识点
# 控制台输入
# 强制类型转换
# int和str是不能比较的
