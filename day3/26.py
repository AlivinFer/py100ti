# 冒泡排序（两两比较，将值大的元素交换到右边，每一轮确定一个最大值）
# 优点：每进行一轮排序，就会少比较一次，就能确定一个最大值，为稳定排序
# 时间复杂度：最优的情况，刚好正序，走一趟就确定，为 O（n）；最差的情况，刚好反序，为 O(n^2)；所以平均复杂度为 O(n^2)
def bubble_sort(a: list):
    for i in range(len(a)):
        count = 0
        for j in range(len(a)-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                count += 1
        if count == 0:
            break
    return a

# 快速排序(先从数列中取出一个数作为基准数，以它进行分区，左边为小于它的数，右边为大于它的数；
# 再对左右区间重复第二步，直到各区间只有一个数) -- 分治法
# 时间复杂度：O(nlogn)
def quick_sort(self, a: list, first: int, last: int):
    # 终止条件
    if first >= last:
        return
    low = first
    high = last
    mid_value = a[low]  # 以首元素作为主元
    while low < high:
        while low < high and a[high] >= mid_value:
            # 左移，找到一个不大于主元的值
            high -= 1
        a[low] = a[high]
        while low < high and a[low] < mid_value:
            # 右移，找到一个大于主元的值
            low += 1
        a[high] = a[low]
    # 循环退出时，low == high
    a[low] = mid_value

    # 递归调用，对mid_value两边的元素进行快排
    self.quick_sort(a, first, low - 1)
    self.quick_sort(a, low + 1, last)


if __name__ == "__main__":
    test = [7, 6, 2, 3, 2, 5, 9, 1, 0, 8]
    print(bubble_sort(test))
