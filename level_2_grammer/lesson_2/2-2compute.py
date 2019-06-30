#Python计算小游戏
import random
print("本游戏是一个计算小游戏，共有5道计算题，一道题1分，满分5分")
score=0 #初试分数
a = random.randint(1, 10)
b = random.randint(1, 10)
c = int(input("第一题：请问%d + %d = ?\n" %(a, b)))
if c==a+b:
    print("回答正确！加1分")
    score=score+1
else:
    print("回答错误，不给分！")
a = random.randint(1, 50)
b = random.randint(1, 50)
c = int(input("第二题：请问%d - %d = ?\n" %(a, b)))
if c == a-b:
    print("回答正确！加1分")
    score=score+1
else:
    print("回答错误，不给分！")
a = random.randint(1, 50)
b = random.randint(1, 50)
c = int(input("第三题：请问%d x %d = ?\n" %(a, b)))
if c == a*b:
    print("回答正确！加1分")
    score=score+1
else:
    print("回答错误，不给分！")
a = random.randint(1, 100)
b = random.randint(1, 100)
c = int(input("第四题：请问%d x %d = ?\n" %(a, b)))
if c == a*b:
    print("回答正确！加1分")
    score=score+1
else:
    print("回答错误，不给分！")
a = random.randint(1, 100)
b = random.randint(1, 100)
c = int(input("最后一题：请问(%d-%d) x (%d+%d) = ?\n" %(a, b, b, a)))
if c == (a-b)*(a+b):
    print("回答正确！加1分")
    score=score+1
else:
    print("回答错误，不给分！")
print("你的最终得分是：", score)
