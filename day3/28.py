# 向一个排好序的数组插入一个数，并使得原数组顺序不变
def insert_a_number(a: list, number):
    length = len(a)
    if number > a[length-1]:
        a.append(number)
    else:
        for i in range(length):
            if number < a[i]:
                a.insert(i, number)
                break
    return a


if __name__ == "__main__":
    a = [0, 5, 6, 7, 9, 10, 12, 15]
    print(insert_a_number(a, 11))
