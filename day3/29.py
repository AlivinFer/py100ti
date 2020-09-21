# 将一个数组逆序输出
def reverse(a: list):
    length = len(a)
    mid = len(a) // 2
    for i in range(mid):
        a[i], a[length-1] = a[length-1], a[i]
        length = length-1
    return a


if __name__ == "__main__":
    a = [0, 4, 2, 6, 1, 5]
    print(reverse(a))