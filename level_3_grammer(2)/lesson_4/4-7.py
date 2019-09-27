# 作业文件：编写一个循环 打印电影院的票价
'''
某家电影院根据观众的年龄段不同收取不同的票价：
3岁(含)以下免费；3~12(含)岁20元；12岁以上30元。
请使用while语句编写一个循环程序，不断询问用户的年龄。
'''
prompt = "\n请输入您的年龄(输入“退出”结束询问)："

while True:
    age = int(input(prompt))

    if age <= 3:
        print("您可以不用购票！")
    elif 3 < age <= 12:
        print("您购票需要花费20元！")
    elif age > 12:
        print("您购票需要花费30元！")
    else:
        continue
