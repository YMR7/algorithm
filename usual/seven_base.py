# -*- coding: utf-8 -*-

"""
给定任意两个7进制的非负正数字符串，要求编写代码返回相加结果的7进制字符串。
输入描述:
输入为空格分开的两个字符串，按字符串拆分即得到两个参数，
如输入为“361 512，拆分后为"361"和"512"，此输入合法。如果输入为"abc def"则不合法。

输出描述:
输出按7进制相加的结果字符串，如果输入不合法，返回“NA”。
示例1输入输出示例仅供调试，后台判题数据一般不包含示例
输入
361 512

输出
1203

说明
输入输出均按照字符串处理。
"""


def test(strs):
    try:
        if not strs:
            return 'NA'
        a = int(strs[0])
        b = int(strs[1])

        first = list(strs[0])[::-1]
        second = list(strs[1])[::-1]
        length_f = len(first)
        length_s = len(second)
        # first 更短
        if length_f > length_s:
            first, second = second, first
            length_s, length_f = length_f, length_s
        res = []
        flag = 0
        for i in range(length_f):
            temp = int(first[i]) + int(second[i])
            need_append = str(flag + (temp % 7))
            res.append(need_append)
            flag = temp // 7
        # leave = second[length_f:]
        # length = len(leave)
        for j in range(length_f, length_s):
            temp = int(second[j]) + flag
            flag = temp // 7
            need_append = str(temp % 7)
            res.append(need_append)
        if flag == 1:
            res.append(str(1))
        return ''.join(res[::-1])
    except:
        return 'NA'


if __name__ == '__main__':
    line = input().split()
    print(test(line))