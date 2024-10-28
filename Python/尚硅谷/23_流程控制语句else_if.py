# _*_ coding : utf-8 _*_
# @Time : 2024/2/21 8:08 PM
# @Author : 叶轩
# @File : 23_流程控制语句else_if
# @Project : Python基础


# 如果您考试考了90以上  成绩为优秀
# 如果您考试考了80以上  成绩为良好
# 如果您考试考了70以上  成绩为中等
# 如果您考试考了60以上  成绩为合格
# score = int(input('请输入您的成绩'))

# 错误写法
# if score >= 90:
#     print('优秀')
# if score >= 80:
#     print('良好')
# if score >= 70:
#     print('中等')
# if score >= 60:
#     print('合格')
# if score <= 60:
#     print('不合格')


# elif
# 正确写法
score = int(input('请输入您的成绩:'))
if score >= 90:
    print('优秀')
elif score >= 80:
    print('良好')
elif score >= 70:
    print('中等')
elif score >= 60:
    print('合格')
else:
    print('不合格')
