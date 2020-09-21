# 输出年月日。判断这一天是这一年的第几天
year = int(input('year:\n'))
month = int(input('month:\n'))
day = int(input('day\n'))

# 如 1996年7月16日 计算时，将前6个月的天数以及7月的16天相加来求
# 另外还需要考虑闰年这一特殊情况
months = (0, 31, 59, 90, 120, 151, 181, 212, 243, 273, 304, 334)
if 1 <= month <= 12:
    sum1 = months[month-1]
else:
    print('data error, input again please')
sum1 += day
leap = 0
if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 == 0)):
    leap = 1
if (leap == 1) and (month > 2):
    sum1 += 1
print('it is the %dth day.' % sum1)
