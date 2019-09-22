# 上学期的外星人程序
from turtle import *

aliens = [{"颜色":"green", "点数":5, "眼睛":"white"},{"颜色":"yellow", "点数":10, "眼睛":"blue"},
          {"颜色":"red", "点数":15, "眼睛":"black"}, {"颜色":"purple", "点数":20, "眼睛":"pink"},
          {"颜色":"black", "点数":30, "眼睛":"white"}]
alien_killed = aliens[int(input("请输入的射杀的外星人的编号："))]
print("你射杀了一个" + alien_killed["颜色"] + "的外星人！获得的点数是：" + str(alien_killed["点数"]))

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
