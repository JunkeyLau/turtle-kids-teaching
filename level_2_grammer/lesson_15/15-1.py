from turtle import *

speed(0)
penup()
right(90)
forward(150)
left(90)
pendown()
color("red","red")
begin_fill()
left(55)
circle(600, 25)
circle(100,200)
circle(600, 25)
end_fill()

# 眼睛
# 移动画笔 
penup()
circle(600,-20)
left(90)
forward(20)
right(150)
pendown()
color("black", "black")
begin_fill()
left(55)
circle(90, 25)
circle(15,200)
circle(90, 25)
end_fill()
# 右边的
penup()
setheading(0)
forward(140)
left(130)
pendown()
begin_fill()
left(55)
circle(90, 25)
circle(15,200)
circle(90, 25)
end_fill()
# 鼻子
done()