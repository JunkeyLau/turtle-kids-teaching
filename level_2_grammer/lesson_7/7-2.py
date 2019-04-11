# 创建数字列表 range()创建的不是列表
# 我们用list()将range()生成的数字创建成为列表
numbers = list(range(1,11))
print(numbers)

# 指定步长
# 打印1~10内的偶数
even_numbers = list(range(2, 11, 2))  # 指导互动
print(even_numbers)
# 引导奇数 list(range(1, 10, 2))