# if-else语句
# 正式学习 if-else 语句类型
# 问题：如果我们需要我们的门铃程序能够针对我们相见的人作出开门欢迎的回应的话，需要如何执行呢？
# 智能门铃
''' 如果在家想享受一个不被打扰的周末，不希望被门铃打扰，
但是又不可以拒绝所有人的上门拜访，例如父母，那么假如现在有一个智能门铃可以进行人脸识别，
能够识别是你的父母还是你的朋友或同事，从而自动回应：“主人在休息请勿打扰！” 的消息，
请问怎么在得知对方身份后怎么针对不同情况做出回应呢？
'''

# Python的不相等语句
visitor = input("请输入来访者：")

if visitor != "父母":
    print("主人在休息请勿打扰！")
else:
    print("欢迎来访！")