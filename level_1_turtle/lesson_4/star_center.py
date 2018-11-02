from turtle import * # 导入turtle模块
screensize(300, 300) # 设置一个300*300的画布
speed(1) # 设置画笔速度为1（最慢）
penup() # 提起画笔
goto(-100,0) # 将画笔往左移动100个单位
pendown() # 放下画笔
pencolor("yellow") # 设置画笔颜色为黄色
fillcolor("yellow") # 绘制星星 设置填充的颜色
begin_fill() # 开始填涂颜色
forward(200) # 画星星
right(144)
forward(200)
right(144)
forward(200)
right(144)
forward(200)
right(144)
forward(200)
end_fill() # 结束涂色
done() # 结束绘图
