#使用Python的字典功能制作一个可以添加新单词的词典
dict = {
    "apple" : "苹果",
    "pear" : "梨",
    "banana" : "香蕉",
    "grape" : "葡萄",
    "watermelon" : "西瓜",
    "orange" : "橘子",
    0 : 0
} #创建一个包含了单词和中文意思的词典
en = input("请输入你想翻译的单词（英语）：") #将输入的内容赋值给en
for word in dict.keys(): #一个for循环，用于遍历dict中的键
    if en == word: #如果某个键与我们要查询的单词是一样的，则满足条件
        ch = dict[word] #将这个键对应的值，也就是这个单词的中文意思赋值给ch
        print(en + "的中文意思是：" + ch) #打印出这个中文意思
        break #跳出循环
    elif 0 == word: #如果到了最后一个单词，那么我们则执行没有该单词的指令
        print("词库中没有此单词！")
    else:
        continue #其它情况，继续循环