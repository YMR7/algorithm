import typing


from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        dp = [[0, 0] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            if i - 2 == -1:
                dp[i][1] = max(dp[i - 1][1], 0 - prices[i])
            else:
                dp[i][1] = max(dp[i - 1][1], dp[i - 2][0] - prices[i])
        return dp[size - 1][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        dp_i_0 = 0
        pre_dp_i_0 = 0
        dp_i_1 = -prices[0]
        for price in prices[1:]:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, pre_dp_i_0 - price)
            pre_dp_i_0 = temp
        return dp_i_0


ans = Solution().maxProfit([1, 2, 3, 0, 2])
print(ans)
