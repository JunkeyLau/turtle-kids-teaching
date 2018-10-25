# Python-Turtle 绘图入门

## 前言
　　在学习Python的过程中，如果需要用到绘图工具，那么就需要使用到Python的turtle库，turtle库是Python中一个很流行的绘图函数库，主要是依据坐标轴来绘制图像，画笔则是一只小海龟，通过控制海龟的在坐标平面的移动，从而绘制各种各样的图像。

## Turtle绘图基础知识
**1. 画布（cancas)**
　　画布顾名思义即用于绘画的区域，在turtle中，我们可以设置画布的初始大小和小海龟的起始位置。

**设置画布大小**
　　`turtle.screensize(canvwidth=None, canvheight=None, bg=None)  
//分别表示画布的宽度，高度和背景颜色（长度单位是像素）`
例如，要设置一个宽800像素，高600像素，背景颜色为灰色的画布
　　` turtle.screensize(800, 600, "grey") `
另外一种表达方式是通过画布所占屏幕比例来设置画布大小，例如，我们需要设置一个占屏幕一半宽，一半高的画布，代码如下
　　` turtle.setup(width=0.5, height=0.5) `
如需定义坐标原点位置，则代码如下
　　` turtle.setup(width=0.5, height=0.5, startx=100, starty=100) //表示的是坐标原点距离窗口左上角顶点的位置，若不填的话则为屏幕中央 `

**2. 画笔**

**2.1 画笔起始位置**
　　在画布上，turtle画笔的起始位置为坐标轴的原点，若设置画布时没有定义原点位置，则原点为画布中心位置。画笔的形状是一个小海龟（箭头），初始方向为x轴的正方向。

**2.2 画笔的属性**
　　画笔的属性包括：画笔的颜色、线条的宽度，画笔的移动速度等

|函数|说明|
|----|----|
|turtle.pensize()|设置画笔的宽度（像素）|
|turtle.pencolor()|没有参数传入，返回当前画笔颜色，传入参数设置画笔颜色，可以是字符串如"green", "red",也可以是RGB代码。|
|turtle.speed()|画笔的移动速度，数值范围为 0-9 ，从1-9速度逐渐加快，0最快|

**2.3 绘图命令**
　　使用海归绘图的命令，主要分为以下三种：
  - 画笔运动命令
  - 画笔控制命令
  - 全局控制命令

**<center>2.3.1 画笔运动命令</center>**

|函数|说明|
|----|----|
|turtle.forward(distance)|向当前的画笔方向移动distance长度|
|turtle.backward(distance)|向当前画笔相反方向移动distance长度|
|turtle.right(degree)|顺时针旋转degree度|
|turtle.left(degree)|逆时针旋转degree度|
|turtle.pendown()|放下笔触，移动时绘制图像|
|turtle.penup()|提起笔触，移动时不绘制图像|
|turtle.goto(x,y)|移动画笔到点(x,y)|
|turtle.circle(±r)|画圆，r为半径，正负表示圆心在画笔的左右|
|dot(r)|绘制一个指定颜色和半径的原点|
|setx()|移动x轴到指定位置|
|sety()|移动y轴到指定位置|
|setheading(angle)|设置当前朝向angle角度|
|home()|设置当前位置为原点，方向向x轴正方向|

**<center>2.3.2 画笔控制命令</center>**

|函数|说明|
|----|----|
|turtle.fillcolor(colorstring)|绘制图形的填充颜色|
|turtle.color(color1, color2)|同时设置pencolor=color1, fillcolor=color2|
|turtle.filling()|返回是否在填充状态|
|turtle.begin_fill()|准备开始填充图形|
|turtle.end_fill()|填充完成|
|turtle.hideturtle()|隐藏画笔的turtle形状|
|turtle.showturtle()|显示画笔的turtle形状|

**<center>2.3.3 全局控制命令</center>**

|函数|说明|
|----|----|
|turtle.clear()|清空turtle窗口，但不改变画笔的位置和状态，即清楚窗口中已做出的图像|
|turtle.reset()|清空窗口并重置turtle为起始状态|
|turtle.undo()|撤销上一个turtle操作|
|turtle.isvisible()|返回turtle是否可见|
|stamp()|复制当前图形|
|turtle.write(string, [font=("font_name", font_size, "font_type")])|写文本，string为文本内容，font是字体的参数，分别为字体名称，大小和类型；font为可选项，font参数也是可选项|

**<center>2.3.4 其他命令</center>**

|函数|说明|
|----|----|
|turtle.mainloop() or turtle.done()|启动事件循环 调用Tkinter的mainloop函数。必须是乌龟图形程序中的最后一个语句。|
|turtle.mode(mode=None)|设置turtle模式（“standard”，“logo”或“world”）并执行重置。如果没有给出模式，则返回当前模式。<table><thead><tr><th>模式</th><th>初始turtle方向</th><th>正方向角度</th></tr></thead><tbody><tr><td>standard</td><td>向x轴正方向（东）</td><td>逆时针</td></tr><tr><td>logo</td><td>向y轴正方向（向北）</td><td>顺时针</td></tr></tbody></table>|
|turtle.delay(delay=None)|设置或返回以毫秒为单位的绘图延迟|
|turtle.begin_poly()|开始记录多边形的顶点,当前画笔位置为第一个顶点|
|turtle.end_poly()|停止记录多边形的顶点，当前画笔位置为多边形的最后一个顶点，将与第一个顶点相连|
|turtle.get_poly()|返回最后记录的多边形|

**3. 命令举例**

   ` turtle.circle(radius, extent=None, steps=None) //给定半径画圆 `
    
   参数说明：
   - radius(半径)：半径为正(负)，表示圆心在画笔的左边(右边)画圆；
   - extent(弧度) (optional)；
   - steps (optional) (做半径为radius的圆的内切正多边形，多边形边数为steps)。
   
   应用举例:
   - circle(50)   整圆;
   - circle(50,steps=3)  三角形;
   - circle(120, 180)  半圆。