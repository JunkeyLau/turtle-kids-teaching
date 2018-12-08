# python的选择语句
n = input("请输入一个数字：")
n = int(n)
if n > 5:
    print("请输入一个小一点的数字：")
    n = input()
    n = int(n)    
else n < 5 :
    print("请输入一个大一点的数字：")
    n = input()
    n = int(n)