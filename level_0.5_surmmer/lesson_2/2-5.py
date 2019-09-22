# 黑白
from MyQR import myqr
myqr.run(
    words='Python',
    picture="猪.png",
    save_name='artiistlc.png'
)

# 彩色
from MyQR import myqr
myqr.run(
    words='https://www.baidu.com',
    picture="圣诞帽 呆.png",
    colorized=True,
    save_name='artiistlc_color.png'
)

# 动态
from MyQR import myqr
myqr.run(
    words='https://www.baidu.com',
    picture="gakki.gif",
    colorized=True,
    save_name='animated.gif'
)