from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        li = []
        self.backtrack(nums, li)
        return self.res

    def backtrack(self, nums, track):
        size = len(nums)
        if size == len(track):
            temp = track.copy()
            self.res.append(temp)
            return
        for num in nums:
            if num in track:
                continue
            track.append(num)
            self.backtrack(nums, track)
            track.pop()


if __name__ == "__main__":
    res = Solution().permute([1, 2, 3])
    print(res)
