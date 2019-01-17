import qrcode #导入qrcode模块
img = qrcode.make("https://www.baidu.com")
 #括号和引号里边的内容是我们需要在这个二维码里边添加的内容
img.save("baidu.png") 
#将我们的图片保存到电脑上，括号和引号里边的内容是图片文件的名字一定要有.png后缀