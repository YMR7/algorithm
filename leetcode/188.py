from typing import List


class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        # 相当于不限交易次数
        if k >= size // 2:
            return self.maxProfit_infinity(prices)
        dp = [[[0, 0] for i in range(k + 1)] for j in range(size)]
        dp[0][0][0] = 0
        dp[0][0][1] = -prices[0]
        for i in range(size):
            for j in range(k, -1, -1):
                dp[i][j][0] = max(dp[i - 1][j][0], dp[i - 1][j][1] + prices[i])
                dp[i][j][1] = max(dp[i - 1][j][1], dp[i - 1][j - 1][0] + prices[i])
        return dp[size - 1][k][0]

    def maxProfit_infinity(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        res = 0
        pre = prices[0]
        for num in prices[1:]:
            if num > pre:
                res = res + (num - pre)
            pre = num
        return res