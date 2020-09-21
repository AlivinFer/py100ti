# 输入星期几的第一个字母，判断一下是星期几，如果第一个字母一样，则输入第二个字母进行判断
from sys import stdin
# python 中标准输入，输入的无论什么都会转换成字符和字符串
letter = stdin.read(1)
stdin.flush()
while letter != 'Y':
    if letter == 'M':
        print("Monday")
        break
    elif letter == 'W':
        print("Wednesday")
        break
    elif letter == 'F':
        print("Friday")
        break
    elif letter == 'T':
        print("please input second letter:")
        letter = stdin.read(1)
        stdin.flush()
        if letter == 'u':
            print("Tuesday")
            break
        elif letter == 'h':
            print("Thursday")
            break
        else:
            print("data error")
            break
    elif letter == 'S':
        print("please input second letter")
        letter = stdin.read(1)
        stdin.flush()
        if letter == 'a':
            print("Saturday")
            break
        elif letter == 'u':
            print("Sunday")
            break
        else:
            print("data error")
