"""
有一排正数，玩家A和玩家B都可以看到。
每位玩家在拿走数字的时候，都只能从最左和最右的数中选择一个。
玩家A先拿，玩家B再拿，两人交替拿走所有的数字，
两人都力争自己拿到的数的总和比对方多。请返回最后获胜者的分数。

例如：
5,2,3,4
玩家A先拿，当前他只能拿走5或者4。
如果玩家A拿走5，那么剩下2，3，4。轮到玩家B，此时玩家B可以选择2或4中的一个，…
如果玩家A拿走4，那么剩下5，2，3。轮到玩家B，此时玩家B可以选择5或3中的一个，…

"""


def test(nums):
    size = len(nums)
    if size == 0:
        return 0
    elif size == 1:
        return nums[0]
    elif size == 2:
        return max(nums)
    else:
        the_sum = sum(nums)
        dp = [[0 for i in range(size)] for j in range(size)]
        for k in range(size - 1):
            dp[k][k] = nums[k]
            dp[k][k + 1] = max(nums[k], nums[k + 1])
        dp[size - 1][size - 1] = nums[-1]
        for k in range(2, size):
            for j in range(k, size):
                i = j - k
                dp[i][j] = max(nums[i] + min(dp[i + 2][j], dp[i + 1][j - 1]),
                               nums[j] + min(dp[i + 1][j - 1], dp[i][j - 2]))
        return max(dp[0][-1], the_sum - dp[0][-1])


if __name__ == '__main__':
    print(test([4, 7, 2, 9, 5, 2]))
