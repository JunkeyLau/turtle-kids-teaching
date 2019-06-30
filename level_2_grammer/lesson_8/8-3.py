# 复制列表
# 方案一 使用切片
my_food = ["汉堡","薯条","可乐","三明治"]
friend_food = my_food[:]
my_food.append("鸡肉卷")
friend_food.append("牛肉卷")
print("我喜欢的食物有：")
print(my_food)
print("\n我朋友喜欢的食物有：" )
print(friend_food)

# 方案二 使用赋值
my_food = ["汉堡","薯条","可乐","三明治"]
friend_food = my_food
my_food.append("鸡肉卷")
friend_food.append("牛肉卷")
print("我喜欢的食物有：")
print(my_food)
print("\n我朋友喜欢的食物有：" )
print(friend_food)