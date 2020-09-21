# 求100以内的素数
def sushua():
    count = 0
    for i in range(2, 100):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            print("%4d" % i, end="")
            count += 1
            if count % 5 == 0:
                print("\n")


if __name__ == "__main__":
    sushua()
