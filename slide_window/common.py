# -*- coding: utf-8 -*-
"""
滑动
"""


def test(strs, num, char):
    length = len(strs)
    temp = 0
    res = 0
    for i in range(num - 1):
        if strs[i] == char:
            temp += 1
    # length - num 是窗口左指针可遍历的范围
    for j in range(length - num):
        right = j + num - 1
        if strs[right] == char:
            temp += 1
        #  j = 0 时不执行， 每次窗口右移时会判断是否需要减去窗口左边移出的值
        if j - 1 >= 0 and strs[j - 1] == char:
            temp -= 1
        if temp > res:
            res = temp
    return res
