from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        DP
        f(n) = min(f(n-coins[0]), f(n-coins[1]), f(n-coins[2]), ...)
        """
        if amount <= 0:
            return 0
        table = {}
        self.helper(coins, amount, table)
        print(table)
        return table[amount]

    def helper(self, coins, n, memo):
        if n in memo:
            return memo[n]
        if n < 0:
            return -1
        if n == 0:
            return 0
        res = float("inf")
        for coin in coins:
            sub = self.helper(coins, n - coin, memo)
            if sub == -1:
                continue
            res = min(res, sub + 1)
        memo[n] = res if res != float("inf") else -1
        return memo[n]

    def coinChange2(self, coins: List[int], amount: int) -> int:
        
        dp = [amount + 1] * (amount + 1)
        dp[0] = 0
        for i in range(amount + 1):
            for coin in coins:
                if i - coin < 0:
                    continue
                dp[i] = min(dp[i], 1 + dp[i - coin])
        return dp[amount] if dp[amount] != amount + 1 else -1


ans = Solution().coinChange2([1, 2, 5], 11)
print(ans)