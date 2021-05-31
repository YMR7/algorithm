from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_dict = {}
        for inx, num in enumerate(nums):
            other = target - num
            if other in num_dict:
                return [inx, num_dict[other]]
            # 在最后更新字典，确保不会使用同一个数字
            num_dict[num] = inx
        return [-1, -1]