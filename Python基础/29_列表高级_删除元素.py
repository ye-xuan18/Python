# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 12:15 PM
# @Author : 叶轩
# @File : 29_列表高级_删除元素
# @Project : Python基础


# model_list = ['韩東', 'chen(瑞)', '王先一', '蒋家乐', 'lby', '王二博', '张华', '王聪', '郑友韩', '莫舟', '李树豪', '刘俊熙', 'Ryan', '麦麦', '林啸']
#
# print(model_list)
#
# # 根据下标来删除列表中的元素
# # 爬取的数据中有个别数据是我们不想要的  可以通过下标的方式删除
# del model_list[4]
# print(model_list)


# city_list = ['北京', '上海', '深圳', '广州', '武汉', '陕西']
#
# print(city_list)
# # pop是删除列表中的最后一个元素
# city_list.pop()
#
# print(city_list)

movie_list = ['唐三', '小舞', '波塞冬', '修罗神']
print(movie_list)

# 根据元素来删除列表中的数据
movie_list.remove('波塞冬')
print(movie_list)
