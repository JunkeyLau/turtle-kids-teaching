# 继续完善我们的外星人程序
# 增加记分功能
'''
为我们的外星人小程序增加记分功能
输入玩家姓名，提供十次射击机会，共有三种颜色的外星人
因此有三种状态，射中绿色，射中黄色，射中红色和没有射中
射中绿色+5点，黄色+10点，红色+15点，每个人的基础分是0分
需要我们在完成的内容是：
当设计中某一个外星人时，打印增加的点数和当前的总点数
'''
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
    else:
        print("你没有获取到点数！目前的总点数是：" + str(grade))

print(player + "，你最终获得的点数为：" + str(grade))