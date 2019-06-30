# 字典
# 继续我们的外星人项目

# 创建一个外星人
alien_0 = {"颜色": "绿色", "点数": 5}
print(alien_0["颜色"])
print(alien_0["点数"])

# 键值对
# 如果一个玩家射杀了alien_0，那么我们就给他弹出他获得的点数
alien_0 = {"颜色": "绿色", "点数": 5}
print("你射杀了一个" + alien_0["颜色"] + "的外星人！获得的点数是：" + str(alien_0["点数"]))

# 升级成为输入
alien_0 = {"颜色": "绿色", "点数": 5}
alien_killed = locals()[input("请输入的射杀的外星人：")]
print("你射杀了一个" + alien_killed["颜色"] + "的外星人！获得的点数是：" + str(alien_killed["点数"]))