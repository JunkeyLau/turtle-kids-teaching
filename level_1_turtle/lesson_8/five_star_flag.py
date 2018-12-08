from turtle import *
def go_to(x,y):
    '''画笔移动函数'''
    penup()
    goto(x,y)
    pendown()
def star(i):
    '''画星星函数'''
    color("yellow","yellow")
    begin_fill()
    for n in range (1,6):
        forward(i) # 开始画星星
        right(144)
    end_fill()
def square(a,b):
    '''定义一个能画矩形的函数,画笔在矩形中央'''
    penup()
    forward(a/2)
    right(90)
    forward(b/2)
    pendown()
    color("red","red") # 红旗
    begin_fill()
    right(180)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    end_fill()
square(300,200) # 开始画五星红旗
go_to(-130,60) # 第一颗星星
star(60)
go_to(-60,85) # 第二颗星星
star(20)
go_to(-40,60) # 第三颗星星
star(20)
go_to(-40,35) # 第四颗星星
star(20)
go_to(-60,15) # 第五颗星星
star(20)
hideturtle()
done()