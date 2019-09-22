# 送心
from turtle import *

# 设置画笔
pensize(5)

# 圆头
circle(80)

# 身体
right(90)
forward(140)

# 画腿
right(45)
forward(120)
penup()
backward(120)
pendown()
left(135)
forward(80)
right(90)
forward(90)

# 画上面的手
penup()
backward(175)
left(90)
backward(80)
pendown()
forward(100)
left(75)
forward(30)

# 画下面的手
penup()
backward(30)

setheading(-90)
forward(30)
left(15)
pendown()
forward(30)
penup()
backward(30)
right(105)
pendown()
forward(100)

# 画❤️ 一个正方形+两个半圆
penup()
setheading(0)
forward(160)
right(90)
forward(20)
left(90)
pendown()
circle(80,80)

done()