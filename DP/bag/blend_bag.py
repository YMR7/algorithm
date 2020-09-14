# 混合背包

"""
一个旅行者有一个最多能用V公斤的背包，现在有n件物品，它们的重量分别是W1，W2，...,Wn，
它们的价值分别为C1,C2,...,Cn。有的物品只可以取一次（01背包），有的物品可以取无限次（完全背包），
有的物品可以取的次数有一个上限（多重背包）。求解将哪些物品装入背包可使这些物品的费用总和不超过背包容量，且价值总和最大。

输入

第一行：二个整数，V(背包容量，V<=200)，N(物品数量，N<=30)；

第2..N+1行：每行三个整数Wi,Ci,Pi，前两个整数分别表示每个物品的重量，价值，第三个整数若为0，则说

明此物品可以购买无数件，若为其他数字，则为此物品可购买的最多件数(Pi)。

输出

仅一行，一个数，表示最大总价值。

样例输入 

10 3
2  1  0
3  3  1
4  5  4
样例输出 

11
"""


def bag(v, n, weights, values, counts):
    # dp = [0 for _ in range(201)]
    dp = [0 for _ in range(v + 1)]
    for i in range(n):
        if counts[i] == 0:
            for j in range(weights[i], v + 1):
                dp[j] = max(dp[j], dp[j - weights[i]] + values[i])

        else:
            for j in range(counts[i]):

                for k in range(v, weights[i] - 1, -1):
                    dp[k] = max(dp[k], dp[k - weights[i]] + values[i])
    return dp[v]


if __name__ == '__main__':
    v, n = map(int, input().split())
    counts = []
    weights = []
    values = []
    for i in range(n):
        wi, ci, pi = map(int, input().split())
        weights.append(wi)
        values.append(ci)
        counts.append(pi)
    print(bag(v, n, weights, values, counts))
