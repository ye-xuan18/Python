# _*_ coding : utf-8 _*_
# @Time : 2024/2/28 9:34 AM
# @Author : 叶轩
# @File : 02_海龟绘图
# @Project : 尚学堂

import turtle

turtle.showturtle()            # 显示箭头
turtle.write('叶轩,你好')
turtle.forward(300)            # 前进300个像素
turtle.color("green")          # 改变画笔的颜色为green
turtle.left(90)                # 程序左转90度
turtle.forward(300)
turtle.goto(0,0)               # 回到坐标系的原点
turtle.penup()                 # 抬起笔，路径就不会画出来
turtle.goto(0,50)
turtle.pendown()
turtle.circle(100)
turtle.done()                  # 程序结束，可以保持窗口一直存在