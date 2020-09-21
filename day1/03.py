# 一个数加上100后是一个完全平方数，再加上268又是一个完全平方数
import math
for i in range(100000):
    x = int(math.sqrt(i+100))
    y = int(math.sqrt(i+368))
    if (x * x == i+100) and (y * y == i+368):
        print(i)
