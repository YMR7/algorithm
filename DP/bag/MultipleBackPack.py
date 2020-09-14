# -*- coding: utf-8 -*-

"""
# target 背包容量
# C 物品重量
# V 物品价值

C = [3, 2, 6, 7, 1, 4, 9, 5]
V = [6, 3, 5, 8, 3, 1, 6, 9]
Count = [3, 5, 1, 9, 3, 5, 6, 8]  # 每种物品的实现
target = 20
F = [0 for i in range(0, target + 1)]
n = len(C)


def CompleteBackPack(cost, value):
    for i in range(cost, target + 1):
        F[i] = max(F[i], F[i - cost] + value)


def OneZeroBackPack(cost, value):
    for i in reversed(range(cost, target + 1)):
        F[i] = max(F[i], F[i - cost] + value)


def MultipleBackPack(cost, value, count):
    if (cost * count) >= target:  # 当该种物品的个数乘以体积大于背包容量，视为有无限个即完全背包
        CompleteBackPack(C[i], V[i])
        return
    temp_count = 1  # 以上情况不满足，转化为以下情况，具体参考《背包九讲》多重背包的时间优化
    while temp_count < count:
        OneZeroBackPack(temp_count * cost, temp_count * value)
        count = count - temp_count
        temp_count = temp_count * 2  # 转化为1，2，4
    OneZeroBackPack(count * cost, count * value)  # 9个中剩下两个


for i in range(0, n):
    MultipleBackPack(C[i], V[i], Count[i])
print(F[target])
"""


# weights：每种物品的体积
# values：每种物品的价值
# counts：每种物品的数量
def trans(weights, values, counts):  # 转换函数 
    K = len(counts)
    newweights = []
    newvalues = []
    num = sum(counts)
    for i in range(K):
        for j in range(counts[i]):
            newweights.append(weights[i])
            newvalues.append(values[i])
    return num, newvalues, newweights


def bag(counts, capacity, weights, values):
    # 先将多重问题转成0-1问题，利用0-1问题的代码。
    num, newvalues, newweights = trans(weights, values, counts)
    dp = [[0 for j in range(capacity + 1)] for i in range(num + 1)]
    for i in range(1, num + 1):
        for j in range(1, capacity + 1):
            dp[i][j] = dp[i - 1][j]
            if j >= newweights[i - 1] and dp[i][j] < (
                    dp[i - 1][j - newweights[i - 1]] + newvalues[i - 1]):
                dp[i][j] = (dp[i - 1][j - newweights[i - 1]] + newvalues[i - 1])
    return dp[-1][-1]


if __name__ == '__main__':
    target = int(input())  # 背包的体积为target
    weight = list(map(int, input().split()))  # 每个物品的体积
    value = list(map(int, input().split()))  # 对应每个物体的价值
    count = list(map(int, input().split()))  # 每个物品可选择的数量
    print(bag(count, target, weight, value))
    # print(bag([2, 5, 10], 8, [2, 2, 1], [20, 10, 6]))
