#   有一个集合，求其全部子集(包含集合自身)


"""
位图法
"""
def PowerSetsBinary(items):
    N = len(items)
    res = []
    for i in range(2 ** N):  # 子集个数，每循环一次一个子集
        combo = []
        for j in range(N):  # 用来判断二进制下标为j的位置数是否为1
            if (i >> j) % 2:
                combo.append(items[j])
        res.append(combo)
    return res


"""
迭代法
 每次迭代，都是上一次迭代的结果+上次迭代结果中每个元素都加当前迭代元素+当前迭代元素
"""


def getAllSubset2(str):
    if str == None or len(str) < 1:
        return
    arr = []
    arr.append(str[0:1])  # str首元素
    i = 1
    while i < len(str):
        lens = len(arr)
        j = 0
        while j < lens:
            arr.append(arr[j] + str[i])
            j += 1
        arr.append(str[i:i + 1])
        i += 1
    arr.append('')
    return arr


"""
递归
"""

class Solution:
    def subsets(self, nums):
        res = []
        n = len(nums)

        def helper(i, tmp):
            res.append(tmp)
            for j in range(i, n):
                helper(j + 1, tmp + [nums[j]])

        helper(0, [])
        return res