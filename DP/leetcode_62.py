"""
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach
the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?


Above is a 7 x 3 grid. How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 3, n = 2
Output: 3
Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right
Example 2:

Input: m = 7, n = 3
Output: 28

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/unique-paths
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

"""


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        递归，每一步要不向右，要不向下

        """

        # 递归，超时
        # if m == 1 and n == 1:
        #     return 1
        # if m > 1:
        #     turn_right = self.uniquePaths(m - 1, n)
        # else:
        #     turn_right = 0
        # if n > 1:
        #     turn_down = self.uniquePaths(m, n - 1)
        # else:
        #     turn_down = 0
        # return turn_down + turn_right

        # DP， 记忆化搜索
        if m == 1 and n == 1:
            return 1
        if m > 1:
            turn_right = self.uniquePaths(m - 1, n)
        else:
            turn_right = 0
        if n > 1:
            turn_down = self.uniquePaths(m, n - 1)
        else:
            turn_down = 0
        return turn_down + turn_right


if __name__ == '__main__':
    print(Solution().uniquePaths(7, 3))