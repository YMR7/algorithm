# leetcode198
#  最大不连续子序和


class Solution:
    def rob(self, nums):
        last, now = 0, 0
        # 每次循环，计算“偷到当前房子为止的最大金额”
        for num in nums:
            last, now = now, max(last + num, now)
        return now
