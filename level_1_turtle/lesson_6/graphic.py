# python的选择语句
from turtle import * # 导入turtle模块
n = input("请输入想要画的图形：（1代表三角形，2代表正方形）")
n = int(n)
if n == 1:
    screensize(300,300)
    forward(100) # 画一个三角形
    left(120)
    forward(100)
    left(120)
    forward(100)
    right(60)
    done()
elif n == 2 :
    screensize(300,300)
    forward(200) # 画一个正方形
    left(90)
    forward(200)
    left(90)
    forward(200)
    left(90)
    forward(200) 
    done()
else:
    print("请输入正确的数字！")