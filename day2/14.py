# 判断 101-200 之间有多少个素数(即让这个数去除 2 到这个数的开方)
import math
total = 0
leap = 1
for i in range(101, 201):
    x = int(math.sqrt(i))
    for j in range(2, x+1):
        if i % j == 0:
            leap = 0
            break
    if leap == 1:
        total += 1
        print(i)
    leap = 1
print(total)
