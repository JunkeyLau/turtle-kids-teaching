# 绘制纪念碑谷图片
from turtle import *  # 导入turtle

screensize(800,800,"#2F4F4F") # 设置画布大小

def go_to(x,y):
    '''画笔移动函数'''
    penup()
    goto(x,y)
    pendown()

left(60)
forward(10)
