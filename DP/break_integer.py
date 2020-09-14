# -*- coding: utf-8 -*-

# 给定数n，设a+b+c+.. = n, 求abc...的最大值


class Solution:
    # def __init__(self, n):
    #     self.n = n
    #     self.max_n = [0] * n
    #     self.result = 0
    def integerBreak(self, n):
        global result
        if n == 1:
            return 1
        for i in range(1, n):
            # print(result)
            result = max(result, i * (n - i), i * self.integerBreak(n - i))

        return result


if __name__ == '__main__':
    test = Solution()
    result = 0
    print(test.integerBreak(5))
