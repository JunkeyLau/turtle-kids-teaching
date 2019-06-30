import turtle
turtle.screensize(1154, 824, "#8fc3ff")
turtle.speed(0)

# 先定义一些基础函数

def go_to(x, y):
    '''画笔移动函数'''
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()

def pen_move(m, n=0):
    '''画笔前后移动函数，默认向前移动'''
    turtle.penup()
    turtle.forward(m)
    turtle.backward(n)
    turtle.pendown()

def window(a, b):
    '''绘制长为a，宽为b的窗户，起笔为左上角向右'''
    turtle.color("white", "#b0d5e8")
    # 先画外框 并填色
    turtle.pensize(4)
    turtle.begin_fill()
    for n in range(2):
        turtle.forward(a)
        turtle.right(90)
        turtle.forward(b)
        turtle.right(90)
    turtle.end_fill()
    # 画窗户格子
    turtle.pensize(3)
    # 竖立格子
    pen_move(a/2)
    turtle.right(90)
    turtle.forward(b)
    # 横向格子
    turtle.right(90)
    pen_move(a/2)
    turtle.right(90)
    pen_move(b/2)
    turtle.right(90)
    turtle.forward(a)
    turtle.pensize(1)

# 重设坐标原点为画布左上角
x=-557
y=412

# 画右上角的太阳
go_to(372+x, -198+y) # 画圆
turtle.color("#fff381", "#fff381")
turtle.begin_fill()
turtle.circle(48)
turtle.end_fill()
turtle.right(90)
pen_move(10)
turtle.pensize(3)
for n in range(7):# 画周围的线条，使用循环
    turtle.forward(20)
    turtle.left(115)
    pen_move(70.3)
    turtle.right(65)
    pen_move(0,20)

# 画白云一朵 结合之前画云朵的经验
go_to(925+x,-300+y)
turtle.setheading(90)
turtle.color("white","white")
turtle.begin_fill()
pen_move(100)
for n in range(2):
    turtle.circle(20, 180)
    turtle.right(90)
    turtle.circle(25,180)
    turtle.right(90)
    turtle.circle(20, 180)
    turtle.left(180)
turtle.end_fill()

# 画青青草地
# 草地分为三部分，左边圆弧+中间直线+右边圆弧
go_to(5+x,-824+y)
turtle.setheading(60)
turtle.color("#7fc877","#7fc877")
turtle.begin_fill()
turtle.circle(-445,60)
turtle.forward(530)
turtle.circle(-254,90)
turtle.end_fill()

# 画房子
# 先画屋顶
go_to(502+x,-300+y)
turtle.setheading(0)
turtle.pensize(1)
turtle.color("#dedc9f","#ff9b6d")
turtle.begin_fill()
turtle.forward(70)
turtle.left(45)
turtle.forward(215)
turtle.setheading(180)
turtle.forward(70)
turtle.left(45)
turtle.forward(215)
turtle.end_fill()
# 画屋顶上的天线
go_to(680+x,-160+y)
turtle.setheading(90)
turtle.pencolor("black")
turtle.pensize(3)
turtle.forward(40)
turtle.right(90)
turtle.forward(10)
turtle.backward(20)
turtle.forward(10)
turtle.left(90)
for n in range(2):
    turtle.forward(25)
    turtle.right(90)
    turtle.forward(20+2*n)
    turtle.backward(40+5*n)
    turtle.forward(20+3*n)
    turtle.left(90)
turtle.forward(30)
turtle.pensize(1)

# 继续画房子主体 左边长方形部分
go_to(502+x,-300+y)
turtle.color("#dedc9f","#f1f0ad")
turtle.begin_fill()
turtle.setheading(-90)
turtle.forward(300)
turtle.left(90)
turtle.forward(70)
turtle.left(90)
turtle.forward(300)
turtle.end_fill()
# 画门
go_to(525+x, -600+y)
turtle.setheading(90)
turtle.color("#a39f76", "#fbf466")
turtle.begin_fill()
turtle.forward(130)
turtle.right(90)
turtle.forward(25)
turtle.right(90)
turtle.forward(130)
turtle.right(90)
turtle.end_fill()
# 画左边的窗户
go_to(525+x, -320+y)
turtle.setheading(0)
window(25, 70)

# 右边房子主体
go_to(572+x, -300+y)
turtle.setheading(45)
turtle.color("#dedc9f","#f1f0ad")
turtle.begin_fill()
turtle.forward(215)
turtle.right(90)
turtle.forward(215)
turtle.right(45)
turtle.forward(300)
turtle.right(90)
turtle.forward(305)
turtle.right(90)
turtle.forward(300)
turtle.end_fill()
# 画右边的四个窗户
go_to(620+x, -320+y)
turtle.setheading(0)
window(70,70)
go_to(760+x, -320+y)
window(70,70)
go_to(620+x, -460+y)
window(70,70)
go_to(760+x, -460+y)
window(70,70)

turtle.hideturtle() # 隐藏turtle
turtle.done() # 结束画图