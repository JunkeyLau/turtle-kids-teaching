# 复习上节课的考试题目 时间控制在15分钟（总结+讲解）
# 附加题第一题：使用Python的range函数生成1-20内能被2整除的数字列表
number = list(range(2, 21, 2))
print(number)

# 附加题第二题：使用切片提取数字列表number = [1, 4, 5, 6, 3, 7, 6, 8] 
# 的最后三位数字到列表number2，并对number2求和
number = [1, 4, 5, 6, 3, 7, 6, 8]
number2 = number[-3:]
print(number2)
S = sum(number2)
print(S)