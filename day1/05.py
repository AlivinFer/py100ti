# 输入三个整数，按从小到大输出
st = []
for i in range(3):
    x = int(input('integer:\n'))
    st.append(x)
st.sort()
print(st)
