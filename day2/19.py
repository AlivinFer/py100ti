# 用递归计算 n！
def factorial(n):
    if n == 0:
        result = 1
    else:
        result = n * factorial(n - 1)
    return result


m = int(input())
for i in range(m):
    print('%d! = %d' % (i, factorial(i)))
