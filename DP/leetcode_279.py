"""
Given a positive integer n, find the least number of
perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.

Example 1:

Input: n = 12
Output: 3
Explanation: 12 = 4 + 4 + 4.
Example 2:

Input: n = 13
Output: 2
Explanation: 13 = 4 + 9.

"""


class Solution:
    def numSquares(self, n: int) -> int:
        """
        需要判断是否可开方
        :param n:
        :return:
        """
        dp = [i for i in range(n + 1)]

        # # 超时
        # for i in range(2, n + 1):
        #     for j in range(1, i + 1):
        #         temp = j
        #         num = 1
        #         # 等差数列， 判断完全平方数
        #         while temp > 0:
        #             temp -= num
        #             num += 2
        #         if temp == 0:
        #             dp[i] = min(dp[i], j + dp[i - j], 1 + dp[i - j])
        #         else:
        #             dp[i] = min(dp[i], j + dp[i - j])

        # 超时
        # for i in range(1, n + 1):
        #     j = 1
        #     while i - j * j >= 0:
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)
        #         j += 1

        # 超时
        # for i in range(1, n + 1):
        #     for j in range(1, int(i**0.5)+1):
        #         dp[i] = min(dp[i], dp[i - j * j] + 1)

        return dp[n]


if __name__ == '__main__':
    print(Solution().numSquares(13))
