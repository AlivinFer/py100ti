# 输出 9 * 9 乘法表
for i in range(1, 10):
    for j in range(1, 10):
        result = i * j
        print('%d * %d = % -3d' % (i, j, result))
    print('')
