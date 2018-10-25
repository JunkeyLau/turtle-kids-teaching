import turtle # 导入turtle库
t = turtle.Turtle() # 将 turtle.Turtle() 赋值给t
t.speed(0) # 设置速度为0（即最快）
t.pencolor("Turquoise") # 设置画笔的颜色
background=t.getscreen()
background.bgcolor('Teal') # 设置背景颜色

x = 0 # 创造一个初始值为0的变量x
t.up() # 起笔函数（笔移动却不作画）

t.right(45) #向右转45度
t.forward(90) #向前进90个单位长度
t.right(135) #向右转135度

t.down() # 落笔函数（此时相当于把笔放在纸上，移动笔可以作画）
# 设置一个while循环，当x<120时重复执行以下操作
while x < 120:
  t.forward(200)
  t.right(61)
  t.forward(200)
  t.right(61)
  t.forward(200)
  t.right(61)
  t.forward(200)
  t.right(61)
  t.forward(200)
  t.right(61)
  t.forward(200)
  t.right(61)

  t.right(11.1111)
  x = x+1 # 每执行完一次操作就给x加上1，这样就可以让x=120时的时候停止循环

t.done() # 结束画图

turtle.exitonclick()
