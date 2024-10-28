# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 12:28 PM
# @Author : 叶轩
# @File : 30_元组高级
# @Project : Python基础


# model_tuple = ('韩東', '王先一', '蒋家乐', 'lby', '王二博', '张华', '王聪', '郑友韩', '莫舟', '李树豪', '刘俊熙', 'Ryan', '麦麦', '林啸')
# print(model_tuple[0])
# print(model_tuple[1])
# print(model_tuple[2])
# print(model_tuple[3])
# 元组不支持修改里面的内容
# model_tuple[4] = '王一博'
# print(model_tuple)

# model_list = ['韩東', '王先一', '蒋家乐', 'lby', '王二博', '张华', '王聪', '郑友韩', '莫舟', '李树豪', '刘俊熙', 'Ryan', '麦麦', '林啸']
# print(model_list[4])
# model_list[4] = '王一博'
# print(model_list)

# 列表中的元素是可以修改的  而元组中的数据是不可以修改的


a_tuple = (5)

print(type(a_tuple))

# 当元组中只有一个元素时       那么它是整形数据
# 定义只有一个元素的元组，需要在唯一的元素后写一个逗号
b_tuple = (5,)
print(type(b_tuple))
