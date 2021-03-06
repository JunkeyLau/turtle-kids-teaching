# 最后两节课为练习课，通过两节课的学习，最终绘制出小猪佩奇的家
# 第九节课内容：画草坪和蓝天 两朵白云 太阳
from turtle import *
screensize(1154, 824, "#8fc3ff")
speed(5)

# 先定义一些基础函数

def go_to(x, y):
    '''画笔移动函数'''
    penup()
    goto(x, y)
    pendown()

def pen_move(m, n=0):
    '''画笔前后移动函数，默认向前移动'''
    penup()
    forward(m)
    backward(n)
    pendown()

def window(a, b):
    '''绘制长为a，宽为b的窗户，起笔为左上角向右'''
    color("white", "#b0d5e8")
    # 先画外框 并填色
    pensize(4)
    begin_fill()
    for n in range(2):
        forward(a)
        right(90)
        forward(b)
        right(90)
    end_fill()
    # 画窗户格子
    pensize(3)
    # 竖立格子
    pen_move(a/2)
    right(90)
    forward(b)
    # 横向格子
    right(90)
    pen_move(a/2)
    right(90)
    pen_move(b/2)
    right(90)
    forward(a)
    pensize(1)

# 重设坐标原点为画布左上角
x=-557
y=412

# 画右上角的太阳
go_to(372+x, -198+y) # 画圆
color("#fff381", "#fff381")
begin_fill()
circle(48)
end_fill()
right(90)
pen_move(10)
pensize(3)
for n in range(7):# 画周围的线条，使用循环
    forward(20)
    left(115)
    pen_move(70.3)
    right(65)
    pen_move(0,20)

# 画白云一朵 结合之前画云朵的经验
go_to(925+x,-300+y)
setheading(90)
color("white","white")
begin_fill()
pen_move(100)
for n in range(2):
    circle(20, 180)
    right(90)
    circle(25,180)
    right(90)
    circle(20, 180)
    left(180)
end_fill()

# 画青青草地
# 草地分为三部分，左边圆弧+中间直线+右边圆弧
go_to(5+x,-824+y)
setheading(60)
color("#7fc877","#7fc877")
begin_fill()
circle(-445,60)
forward(530)
circle(-254,90)
end_fill()

# 画房子
# 先画屋顶
go_to(502+x,-300+y)
setheading(0)
pensize(1)
color("#dedc9f","#ff9b6d")
begin_fill()
forward(70)
left(45)
forward(215)
setheading(180)
forward(70)
left(45)
forward(215)
end_fill()
# 画屋顶上的天线
go_to(680+x,-160+y)
setheading(90)
pencolor("black")
pensize(3)
forward(40)
right(90)
forward(10)
backward(20)
forward(10)
left(90)
for n in range(2):
    forward(25)
    right(90)
    forward(20+2*n)
    backward(40+5*n)
    forward(20+3*n)
    left(90)
forward(30)
pensize(1)

# 继续画房子主体 左边长方形部分
go_to(502+x,-300+y)
color("#dedc9f","#f1f0ad")
begin_fill()
setheading(-90)
forward(300)
left(90)
forward(70)
left(90)
forward(300)
end_fill()
# 画门
go_to(525+x, -600+y)
setheading(90)
color("#a39f76", "#fbf466")
begin_fill()
forward(130)
right(90)
forward(25)
right(90)
forward(130)
right(90)
end_fill()
# 画左边的窗户
go_to(525+x, -320+y)
setheading(0)
window(25, 70)

# 右边房子主体
go_to(572+x, -300+y)
setheading(45)
color("#dedc9f","#f1f0ad")
begin_fill()
forward(215)
right(90)
forward(215)
right(45)
forward(300)
right(90)
forward(305)
right(90)
forward(300)
end_fill()
# 画右边的四个窗户
go_to(620+x, -320+y)
setheading(0)
window(70,70)
go_to(760+x, -320+y)
window(70,70)
go_to(620+x, -460+y)
window(70,70)
go_to(760+x, -460+y)
window(70,70)

hideturtle() # 隐藏turtle
done() # 结束画图