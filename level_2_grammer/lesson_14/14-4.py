# 将5个外星人制作成为一个列表
aliens = [{"颜色": "绿色", "点数": 5},{"颜色": "红色", "点数": 15},
                {"颜色": "黄色", "点数": 10}]
alien_killed = aliens[int(input("请输入的射杀的外星人："))]
print("你射杀了一个" + alien_killed["颜色"] + "的外星人！获得的点数是：" + str(alien_killed["点数"]))