# time calendar 包的使用
import time
# 每个时间戳以自从 1970年1月1号开始计算（以秒为单位）
start = time.time()
print(start)

# 获取当前时间
localtime = time.localtime(time.time())
print(localtime)

# 获取格式化的时间
formal_time = time.asctime(time.localtime(time.time()))
print(formal_time)

# 获取某月日历
import calendar
cal = calendar.month(2020, 10)
print(cal)

for i in range(1000):
    i += 1
end = time.time()
print(end-start)
