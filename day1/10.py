# 判断素数（用一个数去除以2到这个数的平方根）
import math
leap = 1
for i in range(101, 201):
    k = int(math.sqrt(i))
    for j in range(2, k+1):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        print('%-4d' % i)
    leap = 1
