# 数值输入
age = input("你今年几岁？")
print(age)
# 在shell中输入 age >= 18

age = input("你今年几岁？")
age = int(age)
if age >= 18:
    print("你是一个成年人！")
else:
    print("你还未成年！")