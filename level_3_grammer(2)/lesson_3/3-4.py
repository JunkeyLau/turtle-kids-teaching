# 求模运算%
'''
4 % 3
5 % 3
6 % 3
'''

number = int(input("请输入一个数字，我会告诉你它的奇偶："))

if number % 2 == 0:
    print(str(number) + "是一个偶数")
else:
    print(str(number) + "是一个奇数")