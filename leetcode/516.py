class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        # dp[i][j] 代表 s[i:j+1] 最长回文子序列
        size = len(s)
        dp = [[0] * size for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1
        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
        print(dp)
        return dp[0][-1]


ans = Solution().longestPalindromeSubseq('bbbab')
print(ans)