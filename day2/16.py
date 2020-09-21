# 计算 s = a + aa + aaa + aaaa + ... + aa...a
# 用 n 来控制几个数
from functools import reduce
a = int(input())
n = int(input())
s = 0
add = []
for count in range(n):
    s = s + a
    a = a * 10
    add.append(s)
print(reduce(lambda x, y: x+y, add))

