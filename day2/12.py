# 将一个正整数分解成质因数
from sys import stdout
n = int(input("input a number:\n"))
print("%d=" % n)
for i in range(2, n+1):
    while i != n:
        if n % i == 0:
            stdout.write(str(i))
            stdout.write('*')
            n = n // i
        else:
            break
print('%d' % n)

