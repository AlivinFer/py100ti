# 求 3*3 的矩阵对角线元素之和
sum = 0.0
a = []
for i in range(3):
    a.append([])
    for j in range(3):
        a[i].append(float(input("input a number:")))
for k in range(3):
    sum += a[k][k]
print(a)
print(sum)
