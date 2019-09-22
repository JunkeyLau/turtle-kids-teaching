# input()函数
message = input("输入你想说的话，我会帮你把这些话打印出来：")
print(message)

# 用input函数获取信息并调用
name = input("请输入的姓名：")
print("你好，" + name + "！")

# 将提示语句存储在一个变量中，通过inpute调用
prompt = "如果你能告诉我你是谁，我就能够根据你的信息给你回复。"
prompt += "\n请输入你的姓名："
name = input(prompt)
print("\n你好，" + name + "！")
