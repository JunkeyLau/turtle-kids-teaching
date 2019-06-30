from turtle import *
#导入turtle模块

fd = forward
rg = right
# 分别将turtle中的一些指令赋值给变量，方便调用

screensize(300,300)
# 设置一个300*300像素的画布

# 开始画星星
fd(200)
rg(144)
# 画第一个角

fd(200)
rg(144)
# 画第二个角

fd(200)
rg(144)
# 画第三个角

fd(200)
rg(144)
# 画第四个角

fd(200)
# 将最后两个角连接起来

done()
# 结束画图
