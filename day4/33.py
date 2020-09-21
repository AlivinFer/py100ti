# 加密传输数据，传输规则：
# 1. 每位数字都加上 5
# 2. 用得到的和各自除以 10 得到的余数代替该数字
# 3. 再将第一位和第四位交换，第二位和第三位交换


def encode(number):
    a = [number // 1000, number // 100 % 10, number % 100 // 10, number % 10]

    for i in range(4):
        a[i] += 5
        a[i] %= 10

    for i in range(2):
        a[i], a[3-i] = a[3-i], a[i]

    return a


if __name__ == "__main__":
    b = encode(5823)
    print(b)