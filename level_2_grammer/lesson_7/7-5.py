# 作业
'''
使用Python的range生成1-20内能被3整除的列表
提示：Python的取余运算符为%，例如3%2=1(3/2的余数是1) 需要用到if 判断语句
'''
num = []
for i in range(1, 21):
    if i % 3 == 0:
        num.append(i)
    else:
        continue
print(num)


# 使用Python的range生成1-100内能同时被3和2整除的列表
num_2 = []
for i in range(1, 101):
    if i %6 == 0:
        num_2.append(i)
    else:
        continue
print(num_2)