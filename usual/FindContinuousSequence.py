# -*- coding: utf-8 -*-
"""
题目描述
小明很喜欢数学,有一天他在做数学作业时,要求计算出9~16的和,
他马上就写出了正确答案是100。但是他并不满足于此,他在想究竟
有多少种连续的正数序列的和为100(至少包括两个数)。没多久,他
就得到另一组连续正数和为100的序列:18,19,20,21,22。现在把
问题交给你,你能不能也很快的找出所有和为S的连续正数序列? Good Luck!

输出描述:
输出所有和为S的连续正数序列。序列内按照从小至大的顺序，序列间按照开始数字从小到大的顺序
"""

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        max_length = int((2*tsum)**0.5)
        res = []
        for length in range(max_length, 1, -1):
            # 奇数， 偶数
            if (length % 2 == 1 and tsum % length == 0) or (tsum % length * 2 == length):
                start = (2 * tsum / length + 1 - length) / 2
                res.append(list(range(start, start+length)))
        return res


    # 滑动窗口解法
    def FindContinuousSequence(self, tsum):
        # write code here
        left = 1
        right = 2
        res = []
        while left < right:
            cur_sum = (left + right) * (right - left + 1) / 2
            if cur_sum == tsum:
                res.append(list(range(left, right + 1)))
                left += 1
            elif cur_sum > tsum:
                left += 1
            else:
                right += 1

        return res