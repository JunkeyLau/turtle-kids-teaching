# -*- coding: utf-8 -*

# 打印99乘法表
print('\n'.join([' '.join(['%s*%s=%-2s' % (y,x,x*y) for y in range(1,x+1)]) for x in range(1,10)]))


for x in range(1,10):
    for y in range(1,x+1):
        print("%s*%s=%-2s" % (y,x,x*y), end=' ')
    print("")