"""
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
Output: 7
Explanation: Because the path 1→3→1→1→1 minimizes the sum.

"""

from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        row = len(grid)
        col = len(grid[0])
        if col == 0:
            return 0
        for i in range(row):
            for j in range(col):
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j - 1]
                else:
                    if j == 0:
                        grid[i][j] += grid[i - 1][j]
                    else:
                        grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        return grid[-1][-1]
