# 求一个数加上 100 后是一个完全平方数，再加上 268 又是一个完全平方数
import math
for i in range(10000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+368))
    if x*x == i+100 and y*y == i+368:
        print(i)
