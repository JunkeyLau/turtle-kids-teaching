# 画一个粽子
from turtle import *

# 绘制粽子轮廓
color("green","green") # 设置画笔颜色和填涂颜色
begin_fill() # 开始填涂
right(7.5) # 设置画笔起始移动方向
circle(800, 15)
left(105)
circle(800, 15)
left(105)
circle(800, 15)
end_fill() # 结束填涂

# 画白色的粽线
# 第一条线
circle(800, -7.5) # 现将画笔移动到左边的中间
left(120)
color("white")
pensize(3)
circle(200,30)
# 画第二条线
penup()
circle(200,-30)
right(120)
circle(800, -1.5)
left(30)
pendown()
circle(120,75)
# 画第三条线
penup()
left(18)
backward(25)
pendown()
left(20)
circle(80,80)

penup()
goto(-80, -100)
pendown()
color("black")
write('小凯的作品，祝大家端午安康！', font=("Bradley Hand ITC", 20, "bold"))

hideturtle()# 隐藏画笔

done()