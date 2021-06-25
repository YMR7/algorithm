from typing import List, Sized


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        res = 0
        for i in range(size):
            for j in range(i, size):
                res = max(res, prices[j] - prices[i])
        return res


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        res = 0
        min_num = prices[0]
        for num in prices[1:]:
            if num < min_num:
                min_num = num
            elif res < num - min_num:
                res = num - min_num
        return res


class Solution3:
    def maxProfit(self, prices: List[int]) -> int:
        """ "
        dp[i][0]：当天无股票
        dp[i][1]：当天持有股票
        """
        size = len(prices)
        if size <= 1:
            return 0
        dp = [[0, 0] for _ in range(size)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, size):
            # max(昨天无股票，昨天有股票且今天出售）
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # max(昨天有股票，昨天无股票且今天购买）
            dp[i][1] = max(dp[i - 1][1], -prices[i])
        # dp[size - 1][0] 大于 dp[size - 1][1]，最后一天无股票的收益更大
        return dp[size - 1][0]


ans = Solution3().maxProfit([7, 1, 5, 3, 6, 4])
print(ans)
