# -*- coding: utf-8 -*-

'''
给定一个字符串数组（字符串长度和数组的长度均大于1且小于1024），
所有字符均为大写字母。请问，给定的字符串数组是否能通过更换数组中
元素的顺序，从而首尾相连，形成一个环，环上相邻字符串首尾衔接的字符相同。

输入描述:
一行输入，空格分隔，表示字符串数组。
输出描述:
一行输出，返回true或者false，表示是否可以形成环。
示例1输入输出示例仅供调试，后台判题数据一般不包含示例
输入
复制
CAT TIGER RPC
输出
复制
true
示例2输入输出示例仅供调试，后台判题数据一般不包含示例
输入
复制
CAT RPC
输出
复制
false
'''


def judge(s1, s2):
    if s1[-1] == s2[0]:
        return True
    else:
        return False


def swap(s, a, b):
    temp = s[a]
    s[a] = s[b]
    s[b] = temp


def test(strs, num):
    if num == len(strs):
        return strs
    for i in range(num, len(strs)):
        if num > 0 and judge(strs[num - 1], strs[num]):
            swap(strs, num, i)
            test(strs, num + 1)
            swap(strs, num, i)
        elif num == 0:
            swap(strs, num, i)
            test(strs, num + 1)
            swap(strs, num, i)


if __name__ == '__main__':
    strs_num = input().strip().split()
    flag = test(strs_num, 0)
    if flag:
        print('true')
    else:
        print('false')
