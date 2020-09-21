# 判断一个五位正整数是否是回文数
x = int(input("please a integer number:\n"))
x = str(x)
for i in range(len(x)//2):
    if x[i] != x[-i-1]:
        print("this number is not a huiwenshu")
        break
    if i == (len(x) // 2)-1:
        print("this number is huiwenshu")
