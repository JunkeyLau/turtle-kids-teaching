from turtle import *

screensize(300, 300)
pensize(3)
speed(1)

# 绘制房顶
fillcolor("red")
begin_fill()
forward(200)
left(120)
fd(200)
left(120)
fd(200)
end_fill()

# 绘制房体
fillcolor("grey")
begin_fill()
penup()
left(120)
fd(20)
right(90)
pendown()
fd(160)
left(90)
fd(160)
left(90)
fd(160)
end_fill()

# 窗子
backward(40)
penup()
left(90)
fd(40)
pendown()
fillcolor("white")
begin_fill()
fd(60)
left(90)
fd(60)
left(90)
fd(60)
left(90)
fd(60)
end_fill()

# 窗户格子
backward(30)
left(90)
forward(60)
backward(30)
right(90)
backward(30)
fd(60)
hideturtle()

# 完成作画
done()
