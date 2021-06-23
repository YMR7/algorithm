from typing import List


class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        size = len(piles)
        # dp[i][j][0]: 在 piles[i:j+1]中先手能拿到的石子总数
        # dp[i][j][1]: 在 piles[i:j+1]中后手能拿到的石子总数
        dp = [[[0, 0] for i in range(size)] for j in range(size)]
        # base case，只有一堆石子时的情况
        for i in range(size):
            # 先手拿走石子
            dp[i][i][0] = piles[i]
            # 后手没有石子可拿
            dp[i][i][1] = 0
        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                # 先手先拿左边，拿完后变成后手
                left = piles[i] + dp[i + 1][j][1]
                # 先手先拿右边，拿完后变成后手
                right = piles[j] + dp[i][j - 1][1]
                if left > right:
                    dp[i][j][0] = left
                    dp[i][j][1] = dp[i + 1][j][0]
                else:
                    dp[i][j][0] = right
                    dp[i][j][1] = dp[i][j - 1][0]
        return dp[0][size - 1][0] > dp[0][size - 1][1]