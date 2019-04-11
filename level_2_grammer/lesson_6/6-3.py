# 作业 两个列表 发送不同的问候语
import random
friends = ["俸诚希", "唐瀚宇", "吴泓怿", "贾汶瀚", "常博康", "李子见", "马凌宵", "刘奕辰"]
greetings = ["祝你天天开心！","希望你学习进步！","祝你身体健康！","你会越来越帅！"]
for name in friends:
    n = random.randint(0,3)
    print(name + "," + greetings[n])
    print("愿我们的友谊天长地久！\n")