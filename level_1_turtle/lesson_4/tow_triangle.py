from turtle import * # 导入turtle模块
screensize(300,300)
penup() # 提笔
goto(20,20) # 将画笔向右移动20，向上移动20
pendown() # 放笔
pencolor("green")
forward(100) # 画第一个三角形
left(120)
forward(100)
left(120)
forward(100)
right(60)
penup() # 提笔
goto(-20,-20) # 将画笔向右移动20，向上移动20
pendown() # 放笔
forward(100) # 画第二个三角形
left(120)
forward(100)
left(120)
forward(100)
left(120)
done()