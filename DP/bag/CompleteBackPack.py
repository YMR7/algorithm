# -*- coding: utf-8 -*-

# 完全背包,物品数量不限

# target 背包容量
# C 物品重量
# V 物品价值

# C = [3, 2, 6, 7, 1, 4, 9, 5]
# V = [6, 3, 5, 8, 3, 1, 6, 9]
# target = 15
# F = [0 for i in range(0, target + 1)]
# n = len(C)
#
#
# def CompleteBackPack(cost, value):
#     for i in range(cost, target + 1):  # 这是和01背包唯一的区别 正序遍历
#         F[i] = max(F[i], F[i - cost] + value)
#
#
# for i in range(0, n):
#     CompleteBackPack(C[i], V[i])
# print(F[target])


def bag(target, c, v):
    length = len(c)
    dp = [0 for _ in range(target + 1)]
    for i in range(length):
        for j in range(c[i], target + 1):
            dp[j] = max(dp[j], dp[j - c[i]] + v[i])
    return dp[-1]


if __name__ == '__main__':
    target = input()  # 背包的体积为target
    weight = list(map(int, input().split()))  # 每个物品的体积
    value = list(map(int, input().split()))  # 对应每个物体的价值

    print(bag(target, weight, value))
    # print(bag(16, [5, 4, 7, 2, 6], [12, 3, 10, 3, 6]))
