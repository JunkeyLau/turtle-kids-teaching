from turtle import *
screensize(300,300)
for i in range(1, 4): # 用for循环画三个星星
    for n in range (1,6):
        forward(50) # 开始画星星
        right(144)
    penup()
    forward(70)
    pendown()
done()