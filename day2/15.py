# 统计字符串中的数字、空格、英文字母或其它字符的个数
import string
s = input("input a string:\n")
digit = 0
space = 0
letter = 0
other = 0
for c in s:
    if c.isdigit():
        digit += 1
    elif c.isspace():
        space += 1
    elif c.isalpha():
        letter += 1
    else:
        other += 1
print('digit = %d, space = %d, char = %d, other = %d' % (digit, space, letter, other))


