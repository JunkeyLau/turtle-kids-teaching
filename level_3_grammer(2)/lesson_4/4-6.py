# DIY冰激凌 输入想要在冰激凌里面添加的口味 
# 直到输入确认退出（增加口味限制数为4）
prompt = "请输入你想吃的冰激凌口味：（输入“确认”退出程序）"

n = 0
while True:
    taste = input(prompt)
    
    if taste == "确认":
        break
    else:
        print("你添加了" + taste + "口味")

    n += 1
    if n == 4:
        print("最多添加四种口味！")
        break