# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 7:58 PM
# @Author : 叶轩
# @File : 41_文件的读写
# @Project : Python基础


# 写数据
# write写法
fp = open('test.txt', 'a')
fp.write('hello Handong,i am cool boy\n' * 10)
fp.close()

# 如果我在次运行这段代码  会打印10次还是打印5次呢？
# 如果文件存在 会先清空原来的数据 然后在写
# 我想在每一次执行之后都要追加数据
# 如果模式变为了a 就会执行追加操作


# 读数据
fp = open('test.txt', 'r')
# # # 默认情况下 read是一字节一字节的读  效率比较低
# # content = fp.read()
# # print(content)
#
# # readline是一行一行的读取 但是只能读取一行
# content = fp.readline()
# print(content)
# readlines可以按照行来读取 并且以一个列表的形式返回
# 而列表的数据 是一行一行的数据
content = fp.readlines()
print(content)
fp.close()
