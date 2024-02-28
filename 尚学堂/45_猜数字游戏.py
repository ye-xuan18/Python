# _*_ coding : utf-8 _*_
# @Time : 2024/2/28 9:17 AM
# @Author : 叶轩
# @File : 01_猜数字游戏
# @Project : CBPython


import random

secret = random.randint(1,100)
print('猜数游戏')
tries = 1
while tries <= 6:
    guess = int(input('1-100的数字，第%d次猜，请输入：'% (tries,)))
    if guess == secret:
        print('恭喜你猜对了！你只猜了%d次！\n就是这个:%d!' % (tries,secret))
        break
    elif guess < secret:
        print('不好意思，猜大了！')
    else:
        print('不好意思，猜小了！')
    tries += 1
else:
    print('哎呀，怎么也没猜中！再见')