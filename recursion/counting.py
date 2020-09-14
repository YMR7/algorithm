# -*- coding: utf-8 -*-


# 求a^b
# 快速幂
def counting(a, b):
    res = 1
    while b > 0:
        # 保证最后一步肯定会执行if判断
        # 保证b为奇数时也可正常运行
        if b % 2 == 1:
            res *= a
        a = a * a
        b >>= 1
    return res
