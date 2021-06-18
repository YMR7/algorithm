from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        对每一个数字来说，可选可不选，不选时 f(n) = f(n-1)
        选时 f(n) = 
        """