from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        dp[i][0]：第 i 号不偷
        dp[i][1]：第 i 号偷
        """
        size = len(nums)
        if size == 0:
            return 0
        dp = [[0, 0] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = nums[0]
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1])
            dp[i][1] = dp[i - 1][0] + nums[i]
        return max(dp[size - 1])


class Solution2:
    def rob(self, nums: List[int]) -> int:
        """
        dp_i_0：第 i 号不偷
        dp_i_1：第 i 号偷
        """
        size = len(nums)
        if size == 0:
            return 0
        dp_i_0 = 0
        dp_i_1 = nums[0]
        for num in nums[1:]:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1)
            dp_i_1 = temp + num
        return max(dp_i_0, dp_i_1)


class Solution3:
    def rob(self, nums: List[int]) -> int:
        size = len(nums)
        if size == 0:
            return 0
        if size == 1:
            return nums[0]
        dp = [0] * size
        # 只有一间房屋
        dp[0] = nums[0]
        # 只有两间房屋
        dp[1] = max(nums[0], nums[1])
        for i in range(2, size):
            # 偷当前房屋：i - 2 所获得的钱财 + 当前房屋钱财
            # 不偷当前房屋：i - 1
            dp[i] = max(dp[i - 2] + nums[i], dp[i - 1])
        return dp[-1]


ans = Solution3().rob([1, 2, 3, 1])
print(ans)
