from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: [x[0], -x[1]])
        li = [envlop[1] for envlop in envelopes]
        return self.lengthOfLIS(li)

    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        dp = []
        for num in nums:
            inx = self. binary_seatch_left(dp, num)
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


ans = Solution().maxEnvelopes([[4, 5], [4, 6], [6, 7], [2, 3], [1, 1]])
print(ans)
