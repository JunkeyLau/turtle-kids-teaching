from turtle import *
def square(a,b):
    forward(a)
    left(90)
    forward(b)
    left(90)
    forward(a)
    left(90)
    forward(b)
a = int(input("请输入需要矩形的长："))
b = int(input("请输入需要矩形的宽："))
square(a,b)
done()