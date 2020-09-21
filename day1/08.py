# 输出国际象棋棋盘
import sys  # 主要是针对与python解释器相关的变量和方法
for i in range(8):
    for j in range(8):
        if (i+j) % 2 == 0:
            sys.stdout.write(chr(219))  # 输出相关
            sys.stdout.write(chr(219))
        else:
            sys.stdout.write('')
    print('')
