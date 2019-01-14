#使用Python的字典功能制作一个翻译器
dict = {
    "apple" : "苹果",
    "pear" : "梨"
}

en = input("请输入你想翻译的单词：")

ch = dict[en]

print(ch)