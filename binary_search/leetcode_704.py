from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        size = len(nums)
        left = 0
        right = size - 1
        while left < right:
            # 左中位数,  只有两个数时中位数是左边，左边排除（加一）
            mid = (left + right) >> 1
            """
            有等号的分支不排除中位数，另一个分之排除
            """
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1


if __name__ == '__main__':
    print(Solution().search([-1, 0, 3, 5, 9, 12], 9))
