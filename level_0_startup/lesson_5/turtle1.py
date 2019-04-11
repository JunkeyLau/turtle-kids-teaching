from turtle import *  #导入turtle模块
speed(0) #调节画笔速度为最快，1-9速度依此增加，0最快
pensize(2) #调节画笔粗细为2
bgcolor("black") #设置背景颜色为黑色
colors = ["red","yellow","purple","blue"] #建立一个颜色的数组
tracer(True) #开启画笔轨迹
for x in range (600): #循环画正方形
    forward(2*x)
    color(colors[x % 4])
    left(91)
done() #结束画图