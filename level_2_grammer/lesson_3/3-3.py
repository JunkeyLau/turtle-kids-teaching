#学习列表，以自创人物为例
ET = ["大眼睛", "小短腿", "银色衣服", "光头"]
print(ET)

print(ET[2])
print(ET[1])

ET.append("头大身子小")
print(ET)

del ET[2]
print(ET)

human = ["有头发", "彩色衣服", "长腿"]
print(ET+human)

cre_list = human+ET
print(cre_list)