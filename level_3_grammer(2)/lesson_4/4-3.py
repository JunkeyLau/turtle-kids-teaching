# 使用break退出循环
prompt = "\n输入一个你去过的城市："
prompt += "(输入“退出”退出循环程序)"

while True:
    city = input(prompt)

    if city == "退出":
        break
    else:
        print("我去过" + city + "!")