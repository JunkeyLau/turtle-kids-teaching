# 上节课作业答案
'''
人生的不同阶段
如果一个人的年龄小于2岁,就打印一条消息,指出他是婴儿。
如果一个人的年龄为2~4岁,就打印一条消息,指出他正蹒跚学步。
如果一个人的年龄为4~13岁,就打印一条消息,指出他是儿童。
如果一个人的年龄为13~20岁,就打印一条消息,指出他是青少年。
如果一个人的年龄为20~65岁,就打印一条消息,指出他是成年人。
如果一个人的年龄超过65岁,就打印一条消息,指出他是老年人。 
'''

age = int(input("请输入你的年龄："))

if age > 0 and age < 2:
    print("你是一个婴儿！")
elif age >= 2 and age < 4:
    print("你正在蹒跚学步！")
elif age >= 4 and age < 13:
    print("你是一个儿童！")
elif age >= 13  and age < 20:
    print("你还是青少年！")
elif age >= 20 and age < 65:
    print("你已经是一个成年人了！")
elif age >= 65:
    print("你是一位老人！")