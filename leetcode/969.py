from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def pancakeSort(self, arr: List[int]) -> List[int]:
        self.helper(arr, len(arr))
        return self.res

    def helper(self, arr, n):
        if n == 0:
            return
        max_num = max(arr[:n])
        max_num_inx = arr[:n].index(max_num)
        self.res.append(max_num_inx + 1)
        self.reverse(arr, 0, max_num_inx)
        self.res.append(n)
        self.reverse(arr, 0, n - 1)
        self.helper(arr, n - 1)

    def reverse(self, arr, start, end):
        while start < end:
            arr[end], arr[start] = arr[start], arr[end]
            start += 1
            end -= 1


res = Solution().pancakeSort([3, 2, 1])
print(res)