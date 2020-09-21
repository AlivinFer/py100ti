# 求解所有的水仙花数
for i in range(100, 1000):
    j = i // 100
    k = i // 10 % 10
    s = i % 10
    sum1 = j ** 3 + k ** 3 + s ** 3
    if sum1 == i:
        print(sum1)
