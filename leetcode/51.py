from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [['.' for i in range(n)] for j in range(n)]
        # 此种用法是对同一个 list 的引用
        # board = [["."] * n] * n
        self.backtrack(board, 0)
        return self.res

    def backtrack(self, board, row):
        size = len(board)
        if row == size:
            temp = []
            for li in board:
                temp.append("".join(li))
            # print(temp)
            self.res.append(temp)
            return
        for col in range(size):
            if not self.is_valid(board, row, col):
                continue
            board[row][col] = "Q"
            self.backtrack(board, row + 1)
            board[row][col] = "."

    def is_valid(self, board, row, col):
        size = len(board)
        for i in range(row):
            if board[i][col] == "Q":
                return False
        # 右上
        i, j = row - 1, col + 1
        while i >= 0 and j < size:
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1
        # 左下
        i, j = row - 1, col - 1
        while i >= 0 and j >= 0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        return True


if __name__ == '__main__':
    res = Solution().solveNQueens(4)
    print(res)
    # for line in res[0]:
    #     print(line)