# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 11:56 AM
# @Author : 叶轩
# @File : 28_列表高级_查询
# @Project : Python基础

# # in 是判断某一个元素是否在某一个列表中
# model_list = ['韩東', 'chen(瑞)', '王先一', '蒋家乐', 'lby', '王二博', '张华', '王聪', '郑友韩', '莫舟', '李树豪', '刘俊熙', 'Ryan', '麦麦', '林啸',
#               '伊玖柒', '韩睿']

# # 判断一下在控制台输入的那个数据 是否在列表中
# model = input('请输入您喜欢的模特:')
#
# if model in model_list:
#     print('在')
# else:
#     print('不在,求别处')


# not in
city_list = ['北京', '上海', '深圳', '广州', '武汉', '陕西']

# 在控制台输入您喜欢的球类  然后判断是否在这个列表中
city = input('请输入您想去的城市:')

if city not in city_list:
    print('不在')
else:
    print('在')
