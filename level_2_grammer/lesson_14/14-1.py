# 上节课作业
# 在射杀外星人游戏里面增加黑色外星人，设计中黑色的外星人增加20个点
player = input("请输入玩家姓名：")
grade = 0

for n in range(1,11):
    print("现在是第" + str(n) + "次射杀")
    color = input("请输入你射杀的外星人的颜色：")
    if color == "绿色":
        grade = grade+5
        print("你获得了5个点！目前的总点数是：" + str(grade))
    elif color == "黄色":
        grade = grade+10
        print("你获得了10个点！目前的总点数是：" + str(grade))
    elif color == "红色":
        grade = grade+15
        print("你获得了15个点！目前的总点数是：" + str(grade))
    elif color == "黑色":
        grade = grade+20
        print("你获得了20个点！目前的总点数是：" + str(grade))
    else:
        print("你没有获取到点数！目前的总点数是：" + str(grade))

print(player + "，你最终获得的点数为：" + str(grade))