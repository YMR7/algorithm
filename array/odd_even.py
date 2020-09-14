# -*- coding: utf-8 -*-
"""
输入一个整数数组，实现一个函数来调整该数组中数字的顺序，
使得所有的奇数位于数组的前半部分，所有的偶数位于数组的后
半部分，并保证奇数和奇数，偶数和偶数之间的相对位置不变。
"""
from collections import deque


class Solution:
    def reOrderArray(self, array):
        """
        lengths = len(array)
        for i in range(1, lengths):
            if array[i] % 2 == 1:
                for j in range(i, 0, -1):
                    if array[j - 1] % 2 == 0:
                        temp = array[j - 1]
                        array[j - 1] = array[j]
                        array[j] = temp


        return array
         """
        res = deque()
        length = len(array)
        for j in range(length):
            if array[length-j-1] % 2 == 1:
                res.appendleft(array[length-j-1])
            if array[j] % 2 == 0:
                res.append(array[j])
        return list(res)


if __name__ == '__main__':
    example = Solution()
    print(example.reOrderArray([1, 2, 3, 4]))
