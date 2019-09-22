# 题目：有1、2、3、4个数字，能组成多少个互不相同且无重复数字的三位数？都是多少？
cnt = 0 
for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if i!=j and i!=k and j!=k:
                print(i*100+j*10+k)
                cnt+=1
print cnt

'''
题目：企业发放的奖金根据利润提成。利润(I)低于或等于10万元时，奖金可提10%；
利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可可提成7.5%；
20万到40万之间时，高于20万元的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；
60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，
从键盘输入当月利润I，求应发放奖金总数？
'''
i = int(input('Enter the profit:'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
r = 0
for idx in range(0,6):
    if i>arr[idx]:
        r+=(i-arr[idx])*rat[idx]
        print (i-arr[idx])*rat[idx]
        i=arr[idx]
print(r)

'''
题目：一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在
　　　第10次落地时，共经过多少米？第10次反弹多高？
'''
s = 100.
h = 50.0
for i in range(2,11):
    s += 2*h
    h /= 2
print("the sum length of path:%f"%s)
print("the last height is:%f"%h)

'''
题目：猴子吃桃问题：猴子第一天摘下若干个桃子，当即吃了一半，还不瘾，又多吃了一个
　　　第二天早上又将剩下的桃子吃掉一半，又多吃了一个。以后每天早上都吃了前一天剩下
　　　的一半零一个。到第10天早上想再吃时，见只剩下一个桃子了。求第一天共摘了多少。
'''
n = 1
for i in range(9,0,-1):
    n = (n+1)<<1
print(n)

'''
题目：一个数如果恰好等于它的因子之和，这个数就称为“完数”。例如6=1＋2＋3.编程
　　　找出1000以内的所有完数。
'''
from math import sqrt
n = int(raw_input('input a number:'))
sum = n*-1
k = int(sqrt(n))
for i in range(1,k+1):
    if n%i == 0:
        sum += n/i
        sum += i
if sum == n:
    print ('YES')
else:
    print('NO')