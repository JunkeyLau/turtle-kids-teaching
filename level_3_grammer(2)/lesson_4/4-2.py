# 使用标志
prompt = "\n输入你想说的话，我会帮你把这些话打印出来："
prompt += "\n（输入“退出”退出程序。）"

active = True
while active:
    message = input(prompt)

    if message == "退出":
        active = False
    else:
        print(message)
