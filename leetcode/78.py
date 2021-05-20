from typing import List

"""
result = []
def backtrack(路径, 选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径, 选择列表)
        撤销选择
"""


class Solution:
    def __init__(self) -> None:
        self.res = []

    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        last_num = nums.pop()
        res = self.subsets(nums)
        size = len(res)
        for i in range(size):
            temp = res[i].copy()
            res.append(temp)
            res[-1].append(last_num)
        return res

    def subsets2(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return
        self.backtrack(nums, 0, [])
        return self.res

    def backtrack(self, nums, start, track):
        temp = track.copy()
        self.res.append(temp)
        size = len(nums)
        for i in range(start, size):
            track.append(nums[i])
            self.backtrack(nums, i + 1, track)
            track.pop()


if __name__ == '__main__':
    res = Solution().subsets2([1, 2])
    print(res)
