# 计算 1！+ 2！+ 3！+ ...+ 100!
s = 0
t = 1

for j in range(1, 11):
    t *= j
    s += t
print(s)

