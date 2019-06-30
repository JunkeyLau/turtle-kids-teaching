from turtle import *
def star(i):
    color("yellow","yellow")
    begin_fill()
    for n in range (1,6):
        forward(i) # 开始画星星
        right(144)
    end_fill()
i = input("请输入你需要画的星星的大小：")
i = int(i)
star(i)
done()