from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        # dp[i][k][0]：第i天  最多交易k次 不持有
        # dp[i][k][1]：第i天  最多交易k次 持有
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(size)]

        # 初始化 第0天的时候 持有和不持有其实与交易次数无关 和之前的初始化是一样的
        for k in range(1, 3):
            dp[0][k][0], dp[0][k][1] = 0, -prices[0]

        # 按照天数和交易次数来遍历
        for i in range(1, size):
            for k in range(2, 0, -1):
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
        # 最大值出现在最后一天不持有的情况下
        return dp[size - 1][2][0]


class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        # dp[i][k][0]：第i天  最多交易k次 不持有
        # dp[i][k][1]：第i天  最多交易k次 持有
        dp = [[[0] * 2 for _ in range(2 + 1)] for _ in range(size)]

        # 初始化 第0天的时候 持有和不持有其实与交易次数无关 和之前的初始化是一样的
        for k in range(3):
            dp[0][k][0], dp[0][k][1] = 0, -prices[0]

        # 按照天数和交易次数来遍历
        for i in range(1, size):
            for k in range(3):
                # 买入的时候算作一次交易 这里用到了 k-1 所以k为0要分开讨论
                # 想一想k为0时候的意思 第i天持有而且没有买入过 不可能出现
                dp[i][k][0] = max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
                dp[i][k][1] = (
                    max(dp[i - 1][k][1], dp[i - 1][k - 1][0] - prices[i])
                    if k != 0
                    else -prices[i]
                )
        # 最大值出现在最后一天不持有的情况下
        return dp[size - 1][2][0]


ans = Solution2().maxProfit([5, 7, 2, 7, 3, 3, 5, 3, 0])
print(ans)
