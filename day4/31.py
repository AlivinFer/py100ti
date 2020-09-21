# n 个人围成一圈，顺序排号，从第一个人开始报数（从1到3报数），凡报到3的人退出，求最后留下的是原来第几号的那位
def left_number(n):
    num = []
    for i in range(n):
        num.append(i+1)
    i = 0  # 记录循环的标记
    k = 0  # 控制报数 1、2、3
    m = 0  # 记录退出人数

    while m < n - 1:
        if num[i] != 0:
            k += 1
        if k == 3:
            num[i] = 0  # 将报到 3 的人位置归为 0
            k = 0  # 重新报数
            m += 1  # 记录退出人数
        i += 1
        if i == n:
            i = 0  # 重新开始循环
    while num[i] == 0:
        i += 1
    return num[i]


if __name__ == "__main__":
    print(left_number(8))