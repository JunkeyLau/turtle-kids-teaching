age = input("请输入你的年龄：")
age = int(age)
if age < 12:
    print("你无须购票！")
elif age < 18:
    print("你需要购买半价票！")
else:
    print("你需要购买成人票！")