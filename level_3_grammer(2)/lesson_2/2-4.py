# 将修改外星人用到我们的字典中
# 作业：添加3个外星人
from turtle import *

aliens = []
n = int(input("请输入你想保存到数据库的外星人的个数："))
for i in range(n):
    alien = {}
    alien["颜色"] = input("请输入第"+str(i+1)+"个外星人的颜色(英语)：")
    alien["眼睛"] = input("请输入第"+str(i+1)+"个外星人眼睛的颜色(英语)：")
    aliens.append(alien)

alien_killed = aliens[int(input("请输入的要画的外星人的编号："))-1]

speed(1)
penup()
right(90)
forward(100)
left(90)
pendown()
color(alien_killed["颜色"],alien_killed["颜色"])
begin_fill()
left(55)
circle(600,25)
circle(100,200)
circle(600,25)
end_fill()

# 画眼睛 先画左边的
penup()
color(alien_killed["眼睛"],alien_killed["眼睛"])
circle(600,-20)
left(90)
forward(20)
right(95)
pendown()
begin_fill()
circle(90,25)
circle(15,200)
circle(90,25)
end_fill()
# 右边的眼
penup()
setheading(0)
forward(140)
left(185)
pendown()
begin_fill()
circle(90,25)
circle(15,200)
circle(90,25)
end_fill()
done()
