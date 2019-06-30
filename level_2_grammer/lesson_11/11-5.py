# if-elif-else语句
# 需要针对多个条件作出不同的回应

'''
游乐场的收费标准：
4岁以下免费；
4-12岁收费40元；
12-18岁收费80元；
18岁及以上收费100元。
'''

# 使用if-elif-else语句解决这个问题

age = int(input("请输入你的年龄："))

if age < 4:
    pritn("你进入游乐场不需要购买门票！")
elif age >= 4 and age < 12:
    pritn("你需要支付40元购买门票")
elif age >= 12 and age < 18:
    pritn("你需要支付80元购买门票")
else:
    pritn("你需要支付100元购买门票")
