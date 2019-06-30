#用Python语言解决奥数问题
# 在下面两个算式中，相同的汉字代表相同的数字（1-9），不同的汉字代表不同的数字：
# 数*学=花园， 数+学=探秘，
# 那么“花园探秘” 代表的数学数字是？

print("“花园探秘”所代表的数字的所有可能组合如下：")
numlist = [1,2,3,4,5,6,7,8,9] #新建一个数字列表
for a in numlist: #使用循环遍历这个列表
    for b in numlist:
        for c in numlist:
            for d in numlist:
                for e in numlist:
                    for f in numlist:
                       if  a*b==(10*c+d) and (a+b)==(10*e+f) and a!=b!=c!=d!=e!=f:
                           print(a,b,c,d,e,f) #打印出可能的组合

#变式练习
#a, b , c为从1-9不重复的数字，abc+cba=1333，请问a、b、c分别代表什么数字？