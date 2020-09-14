# 01 背包

"""
def bag(n, c, w, v):

    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            # 不放第i个物品
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            # value[i - 1][j - w[i - 1]]表示放第i个物品后背包剩余容量可以得到的最大价值
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]

    return value[-1][-1]


if __name__ == '__main__':
    a = list(map(int, input().split()))
    n = len(a)
    b = list(map(int, input().split()))
    c = int(input())
    print(bag(n, c, a, b))

"""



"""
def zeroOneBagOpt(num,capacity,weightList,valueList):
    valueRes = [0 for i in range(capacity+1)]
    for i in range(1, num + 1):
        for j in range(capacity, 0, -1):
            if j >= weightList[i-1]:
                valueRes[j] = max(valueRes[j-weightList[i-1]]+valueList[i-1], valueRes[j])
        # i变一次，数组的更新一次，利用数组的不断更新，达到上面的方法动态规划的目的。
        # 当j遍历更新完一遍valueRes，valueRes就相当于完成上边方法中表第i+1行的填充.
        # 必须从后向前遍历和判断储存结果的数组，因为valueRes[j-weightList[i-1]]+valueList[i-1]就相当于V(i-1,j-Wi)+ Vi
        # 判断第i个物品是否是最优解的时候，需要以i-1的情况为基础，不能掺杂有关第i个物品的信息，
        # 如果从前往后遍历，那么valueRes[:j]的数是判断了i之后的，会产生错误。
        # 这里的value[j]即为上一次最佳结果，从后向前可以在遍历到j的未知的时候，不破坏j前面的上一次的最佳结果。
        # 
    return valueRes
print(zeroOneBagOpt(5,10,[2,2,6,5,4],[6,3,5,4,6]))
# 输出结果为：[0, 0, 6, 6, 9, 9, 12, 12, 15, 15, 15]
"""


def bag(n, c, w, v):
    """
    测试数据：
    n = 6  物品的数量，
    c = 10 书包能承受的重量，
    w = [2, 2, 3, 1, 5, 2] 每个物品的重量，
    v = [2, 3, 1, 5, 4, 3] 每个物品的价值
    """
    # 置零，表示初始状态
    value = [[0 for j in range(c + 1)] for i in range(n + 1)]
    for i in range(1, n + 1):
        for j in range(1, c + 1):
            # 不放第i个物品
            value[i][j] = value[i - 1][j]
            # 背包总容量够放当前物体，遍历前一个状态考虑是否置换
            # value[i - 1][j - w[i - 1]]表示放第i个物品后背包剩余容量可以得到的最大价值
            if j >= w[i - 1] and value[i][j] < value[i - 1][j - w[i - 1]] + v[i - 1]:
                value[i][j] = value[i - 1][j - w[i - 1]] + v[i - 1]

    # 放入的物品索引
    y = c
    for x in range(n, 0, -1):
        if value[x][y] > value[x - 1][y]:
            print(x)
            y = y - w[x - 1]

    return value


if __name__ == '__main__':
    print(bag(6, 10, [2, 2, 3, 1, 5, 2], [2, 3, 1, 5, 4, 3]))


