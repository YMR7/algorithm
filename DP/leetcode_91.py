"""
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).
Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

"""


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        和 a，b、、、无关系， 只要知道有 26 个数字可选即可

        细节：要考虑 ‘0’， eg：‘002’应返回 0

        递归： 每次可拿一个数字或两个数字，对每个数字判断是否在区间，可以分完全部数字即是一种方案

        理解： 分2个 和 1 个不会重复计算
        """
        if not s or len(s) == 0:
            return 0
        size = len(s)
        li = [str(i + 1) for i in range(26)]

        # # 无法计算‘12300414’ 的情况
        # if size == 0 or s.startswith('0'):
        #     return 0
        # elif size == 1:
        #     return 1
        #
        # else:
        #     if s[:2] in li:
        #         count = self.numDecodings(s[1:]) + 1
        #     else:
        #         count = self.numDecodings(s[1:])
        #     return count

        return self._count(s, size)

    # 递归
    # def _count(self, s, li, start):
    #     if len(s) == start:
    #         return 1
    #     if s[start] == '0':
    #         return 0
    #     ans1 = self._count(s, li, start + 1)
    #     ans2 = 0
    #     # 还有两个字母
    #     if start < len(s) - 1:
    #         if s[start:start + 2] in li:
    #             ans2 = self._count(s, li, start + 2)
    #     return ans1 + ans2

    # # dp
    # def _count(self, s, size):
    #     dp = [0] * (size + 1)
    #     # 最后两个字母可以组合在一起
    #     dp[-1] = 1
    #     dp[-2] = 0 if s[-1] == '0' else 1
    #     # 倒数第二个字母开始
    #     for i in range(size-2, -1, -1):
    #         if s[i] == '0':
    #             dp[i] = 0
    #             continue
    #         if int(s[i]+s[i+1]) <= 26:
    #             dp[i] = dp[i+1] + dp[i + 2]
    #         else:
    #             dp[i] = dp[i + 1]
    #     return dp[0]

    # dp 空间压缩, 斐波那契数列
    def _count(self, s, size):
        # 最后两个字母可以组合在一起
        a = 1
        b = 0 if s[-1] == '0' else 1
        # 倒数第二个字母开始
        for i in range(size-2, -1, -1):
            if s[i] == '0':
                a = b
                b = 0
                continue
            if int(s[i]+s[i+1]) <= 26:
                temp = b
                b = a + b
                a = temp
            else:
                a = b
        return b


if __name__ == '__main__':
    print(Solution().numDecodings('27'))
