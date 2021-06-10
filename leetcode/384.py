from typing import List
import random


class Solution:

    def __init__(self, nums: List[int]):
        self.nums = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.nums

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        res = self.nums.copy()
        size = len(res)
        for i in range(size):
            tmp = random.randint(0, size - 1)
            res[i], res[tmp] = res[tmp], res[i]
        return res
