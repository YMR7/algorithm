"""
Given a positive integer n, break it into the sum of
at least two positive integers and maximize the product
of those integers. Return the maximum product you can get.

Example 1:

Input: 2
Output: 1
Explanation: 2 = 1 + 1, 1 × 1 = 1.
Example 2:

Input: 10
Output: 36
Explanation: 10 = 3 + 3 + 4, 3 × 3 × 4 = 36.

"""


class Solution:
    def integerBreak(self, n: int) -> int:
        assert n >= 2

        # dp
        dp = [-1] * (n + 1)
        for i in range(2, n+1):
            for j in range(1, i):
                # 分割成 j 和 (i - j)
                dp[i] = max(dp[i], j * (i - j), j * dp[i - j])
        return dp[n]


        # # 数学归纳法
        # if n == 2:
        #     return 1
        # if n == 3:
        #     return 2
        # count = n // 3
        # mod = n % 3
        # if mod == 1:
        #     return 3 ** (count - 1) * 4
        # elif mod == 2:
        #     return 3 ** count * 2
        # else:
        #     return 3 ** count

if __name__ == '__main__':
    print(Solution().integerBreak(4))