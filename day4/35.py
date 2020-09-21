# 字符串的方法
# count: 计数，返回给定字符在字符串当中的个数
# find: 查找，返回从左第一个指定字符的索引，找不到返回 -1
def count_substring(str, sub_str):
    print(str.count(sub_str))
    print(str.find(sub_str))


if __name__ == "__main__":
    count_substring("qwerdfadfeufdfcfhdf", "df")
