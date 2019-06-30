# 猜数字游戏
import random
secret = random.randint(1, 99)
guess = 0
tries = 0
print("Hello! 我是机器人小凯，这是一个猜数字游戏，每一局的数字都是1-99中的任意一个。")
print("我将给你六次机会猜这个随机数，现在就开始吧！")
while guess != secret and tries < 6: # 这是一个while循环
    guess = int(input("请输入你想猜的数字：")) #将我们猜的数字转化成为整形并赋值给变量guess
    if guess < secret:
        print("太小了！换一个大一点的数吧~")
    elif guess > secret:
        print("太大了！试试一个小点的数呢？")
    tries = tries + 1
if guess == secret:
    print("猜中啦！你真厉害！")
else:
    print("你的机会已经用完了！期待下次能有好运吧~")
    print("你要猜的数字是：", secret)