from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        size = len(nums)
        # dp[i] 表示以 nums[i] 为结尾为最长上升子序列
        dp = [1] * size
        for i in range(1, size):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for num in nums:
            inx = self.binary_seatch_left(dp, num)
            if inx == len(dp):
                dp.append(num)
            else:
                dp[inx] = num
        return len(dp)

    def binary_seatch_left(self, dp, target):
        left = 0
        right = len(dp)
        while left < right:
            mid = (left + right) // 2
            if dp[mid] > target:
                right = mid
            elif dp[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left