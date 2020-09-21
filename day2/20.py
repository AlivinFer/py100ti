# 递归计算年龄 第一个人十岁，后面依次比前面一个人大两岁
def age(n):
    if n == 1:
        result = 10
    else:
        result = age(n-1) + 2
    return result


m = int(input())
print(age(m))
