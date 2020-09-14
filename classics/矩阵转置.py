
# N × N 矩阵 旋转， matrix 是二维
class Solution1:
    def rotate(self, matrix):
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix[0])
        # 先转置
        for i in range(N):
            for j in range(i, N, 1):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        # 再每行翻转
        for i in range(N):
            matrix[i].reverse()


class Solution2:
    def rotate(self, matrix):
        n = len(matrix)
        # 水平翻转
        for i in range(n // 2):
            for j in range(n):
                matrix[i][j], matrix[n - i - 1][j] = matrix[n - i - 1][j], matrix[i][j]
        # 主对角线翻转
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]



# 将一个MxN的矩阵存储在一个一维数组中，编程实现矩阵的转置
"""
1. 移动形成了一个环
2. 前驱节点：(i%m)*n + i/m
3. 后继节点：(i%n)*m + i/n
4. 判断环是否重复：一次遍历该环，则第一个下标肯定是这个环中最小的。
        如果一个环被处理过，那么总能找到一个它的后继是小于它的
"""


def get_next(i, m, n):
    return (i % n) * m + i // n


def get_pre(i, m, n):
    return (i % m) * n + i // m


def move(mtx, i, m, n):
    temp = mtx[i]
    cur = i
    pre = get_pre(cur, m, n)
    while pre != i:
        mtx[cur] = mtx[pre]
        cur = pre
        pre = get_pre(cur, m, n)
    mtx[cur] = temp


def start(mtx, m, n):
    size = m * n
    for i in range(size):
        next = get_next(i, m, n)
        # 若存在后继小于i说明重复
        while next > i:
            next = get_next(next, m, n)
        if next == i:
            move(mtx, i, m, n)

