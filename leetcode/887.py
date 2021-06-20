class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def dp(k, n):
            if (k, n) in memo:
                return memo[(k, n)]
            if k == 1:
                return n
            if n == 0:
                return 0
            res = float("inf")
            for i in range(1, n + 1):
                egg_break = dp(k - 1, i - 1)
                egg_full = dp(k, n - i)
                res = min(res, max(egg_break, egg_full) + 1)
            memo[(k, n)] = res
            return res

        memo = {}
        return dp(k, n)


class Solution2:
    def superEggDrop(self, k: int, n: int) -> int:
        # dp[i][j] 鸡蛋数为 k，扔 j 次所能测试的楼高
        dp = [[0] * (n + 1) for _ in range(k + 1)]
        m = 0
        while dp[k][m] < n:
            m += 1
            for i in range(1, k + 1):
                dp[i][m] = dp[i - 1][m - 1] + dp[i][m - 1] + 1
        print(dp[0])
        print(dp[1])
        print(dp[2])
        return m


ans = Solution2().superEggDrop(2, 6)
print(ans)