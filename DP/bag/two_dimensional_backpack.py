# 二维背包

# C1 = [3, 2, 6, 7, 1, 4, 9, 5]
# C2 = [6, 2, 4, 6, 7, 3, 8, 5]
# V = [6, 3, 5, 8, 3, 1, 6, 9]
#
# # Count = [3,5,1,9,3,5,6,8]
# target1 = 20
# target2 = 25
# n = len(C1)
# F = [[0] * (target2 + 1) for i in range(0, target1 + 1)]
# for i in range(0, n):
#     for j in reversed(range(C1[i], target1 + 1)):
#         for m in reversed(range(C2[i], target2 + 1)):  # 逆序遍历
#             F[j][m] = max(F[j][m], F[j - C1[i]][m - C2[i]] + V[i])
#
# print(F[target1][target2])


def bag(capacity_1, capacity_2, weight_1, weight_2, value):
    length = len(value)
    dp = [[0] * (capacity_2 + 1) for _ in range(capacity_1 + 1)]
    for i in range(length):
        for j in reversed(range(weight_1[i], capacity_1 + 1)):
            for k in reversed(range(weight_2[i], capacity_1 + 1)):
                dp[j][k] = max(dp[j][k], dp[j - weight_1[i]][k - weight_2[i]] + value[i])
    return dp[-1][-1]


if __name__ == '__main__':
    target_1 = input()  # 背包的限制target_1
    target_2 = input()  # 背包的限制target_2

    weight_1 = list(map(int, input().split()))  # 物品的限制1
    weight_2 = list(map(int, input().split()))  # 物品的限制2
    value = list(map(int, input().split()))  # 对应每个物体的价值

    print(bag(target_1, target_2, weight_1, weight_2, value))




