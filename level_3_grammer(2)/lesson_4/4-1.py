# 上节课作业
# 何时退出while循环
prompt = "输入你想说的话，我会帮你把这些话打印出来："
prompt += "\n输入“退出”退出程序"

message = ""
while message != "退出":
    message = input(prompt)
    print(message)