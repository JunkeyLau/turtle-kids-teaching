from turtle import *  # 导入Turtle库
screensize(500, 500)  # 设置一个500*500的画布
speed(1)  # 设置画笔速度为1
penup()  # 提笔
goto(-152.5, 50)  # 将画笔向左移动152.5个单位
pendown()  # 放笔
color("red", "red")  # 设置画笔颜色为红色，填涂颜色为红色
begin_fill()  # 开始填涂
forward(300)  # 画红旗
left(90)
forward(150)
left(90)
forward(300)
left(90)
forward(150)
end_fill()  # 结束填涂
color("brown", "brown")  # 设置画笔颜色为棕色，填涂颜色为棕色
begin_fill()  # 开始填涂
forward(250)  # 画旗杆
right(90)
forward(5)
right(90)
forward(400)
right(90)
forward(5)
end_fill()  # 结束填涂
done()  # 结束画图