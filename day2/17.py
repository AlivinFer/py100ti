# 计算一个球从100米高度自由落下，每次落下再反弹的高度为越来的一半，计算第十次反弹的高度以及经过多少米
s = 100
h = s / 2
for n in range(2, 11):
    s += h*2
    h /= 2
print("total:%f" % s)
print("%f" % h)
