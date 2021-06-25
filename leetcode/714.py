from typing import List


class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        dp = [[0, 0] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = -(prices[0] + fee)
        for i in range(1, size):
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - (prices[i] + fee))
        return dp[size - 1][0]


class Solution2:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        dp_i_0 = 0
        dp_i_1 = -(prices[0] + fee)
        for price in prices[1:]:
            temp = dp_i_0
            dp_i_0 = max(dp_i_0, dp_i_1 + price)
            dp_i_1 = max(dp_i_1, temp - (price + fee))
        return dp_i_0


ans = Solution().maxProfit([1, 3, 2, 8, 4, 9], 2)
print(ans)
