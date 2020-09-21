# 企业发放的奖金根据利润提成
# 利润小于等于 10 万元时，奖金可提 10%
# 10-20 万部分，提成 10%
# 20-40 万部分 提成 5%
# 40-60 万部分，提成 3%
# 60-100 万部分，提成 1.5%
# 高于 100 万部分，提成 1%
bonus1 = 100000 * 0.1
bonus2 = bonus1 + 100000 * 0.075
bonus3 = bonus2 + 200000 * 0.05
bonus4 = bonus3 + 200000 * 0.03
bonus5 = bonus4 + 400000 * 0.015
i = int(input("profit:\n"))
if i <= 100000:
    bonus = i * 0.1
elif i < 200000:
    bonus = 100000 * 0.1 + (i-100000) * 0.075
elif i <= 400000:
    bonus = bonus2 + (i-200000) * 0.05
elif i <= 600000:
    bonus = bonus3 + (i-400000) * 0.03
elif i <= 1000000:
    bonus = bonus4 + (i-600000) * 0.015
else:
    bonus = bonus5 + (i-1000000) * 0.01
print('bonus=', bonus)

