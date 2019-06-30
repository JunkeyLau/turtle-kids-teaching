from turtle import *
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "purple"]
speed(0)
def rainbow(i):
    '''画一个半径为i的彩虹，画笔所在位置为圆心'''
    penup()
    forward(i)
    pendown()
    left(90)
    for n in range(7):
        color(colors[n], colors[n])
        begin_fill()
        circle((i-n*(i/30)), 180)
        left(90)
        forward(i/30)
        left(90)
        circle(-(i-(n+1)*(i/30)), 180)
        left(90)
        forward(i/30)
        end_fill()
        penup()
        backward(i/30)
        left(90)
        pendown()
rainbow(150)
done()