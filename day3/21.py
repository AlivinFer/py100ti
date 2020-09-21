# 输入一个不超过5位数的正整数，求它是几位数，并逆序打印出每一位数
def num_reverse():
    x = int(input("please input a number:\n"))
    print("Number of digits:", len(str(x)))
    one_num_list = list(str(x))
    one_num_list.reverse()
    print('\n'.join(one_num_list))


if __name__ == "__main__":
    num_reverse()
