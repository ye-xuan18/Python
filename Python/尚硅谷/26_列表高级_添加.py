# _*_ coding : utf-8 _*_
# @Time : 2024/2/22 11:09 AM
# @Author : 叶轩
# @File : 26_列表高级_添加
# @Project : Python基础


# append   追加   在列表的最后添加一个对象/数据
star_list = ['华晨宇', '陈家淇']
print(star_list)

star_list.append('周深')
print(star_list)

# insert  插入
model_list = ['韩東', 'chen(瑞)', '王先一', '蒋家乐', 'lby']
print(model_list)
# index的值就是你想插入数据的那个下标
model_list.insert(1, '张华')
print(model_list)

# extend
movie_list = ['肖战', '赵丽颖', '任宥纶']
movie1_list = ['唐三', '小舞', '波塞冬', '修罗神']
movie_list.extend(movie1_list)
print(movie_list)
