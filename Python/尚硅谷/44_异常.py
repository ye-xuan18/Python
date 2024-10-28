# _*_ coding : utf-8 _*_
# @Time : 2024/2/23 10:49 AM
# @Author : 叶轩
# @File : 44_异常


# fp = open(test.txt, 'r')
#
# fp.read()
#
# fp.close()
# 异常的格式

# try:
#     可能出现异常的代码
# except 异常的类型
#     友好的提示

try:
    fp = open(test.txt, 'r')
    fp.read()
    fp.close()
except FileNotFoundError:
    print('系统正在升级，请稍后再试')
