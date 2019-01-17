import qrcode #导入qrcode模块
qr = qrcode.QRCode( 
    #创建QRCode类，用于指定二维码的类型
    version=20,  #二维码的版本，有1-40共40个版本
    error_correction=qrcode.constants.ERROR_CORRECT_L, 
    # 二维码的容错率，从低到高分别是L、M、Q、H
    box_size=10, #生成图片的像素
    border=4,  #二维码的边框宽度
)
qr.add_data("搭搭乐乐机器人")
 #括号和引号里边的内容是我们需要在这个二维码里边添加的内容
qr.make(fit=True) 
#将自适应生成二维码开启
img = qr.make_image() 
#制作二维码图片
img.save("测试.png") 
#将我们的图片保存到电脑上，括号和引号里边的内容是图片文件的名字一定要有.png后缀