# 创建一个我们自己能够输入内容的字典
# 以月饼为例
moon_cake = {}
moon_cake["馅料"] = "火腿"
print(moon_cake)


moon_cake = {}
moon_cake["馅料"] = "火腿"
moon_cake["口味"] = "甜咸"
print(moon_cake)

# 创建一个能自己输入馅料的月饼字典列表
moon_cakes = []
for n in range(5):
    moon_cake = {}
    moon_cake["馅料"] = input("请输入第"+str(n+1)+"个月饼的馅料：")
    moon_cake["口味"] = input("请输入第"+str(n+1)+"个月饼的口味：")
    moon_cakes.append(moon_cake)

for n in range(5):
    print("第" + str(n+1) + "个月饼的馅料是：" + moon_cakes[n]["馅料"] + "，口味：" + moon_cakes[n]["口味"])