# 有 n 个整数，使其前面各数顺序后移 m 个位置，最后那 m 个数变成最前面的 m 个数
def move(array: list, m):
    """
    :param array: 用来存储 n 个数的数组
    :param m: 移动 m 个数
    :return: array
    """
    n = len(array)
    array_end = array[n-1]
    for i in range(n-1, 0, -1):
        array[i] = array[i-1]
    array[0] = array_end
    m -= 1
    if m > 0:
        move(array, m)
    return array


if __name__ == "__main__":
    a = [5, 4, 0, 1, 2]
    print(move(a, 2))

