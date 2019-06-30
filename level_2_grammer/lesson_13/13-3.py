# 精简外星人游戏
player = input("请输入玩家姓名：")
grade = 0
ailen_color = ["绿色", "黄色", "红色"]
for n in range(1,11):
    print("现在是第" + str(n) + "次射杀")
    color = input("请输入你射杀的外星人的颜色：")
    for m in range(3):
        if color == ailen_color[m]:
            grade = grade + (m+1)*5
            print("你获得了" + str((m+1)*5) + "点数！目前的总点数是：" + str(grade))
print(player + "，你最终获得的点数为：" + str(grade))