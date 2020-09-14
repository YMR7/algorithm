"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

Your algorithm's runtime complexity must be in the order of O(log n).

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/search-in-rotated-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        时间复杂度要求是 O（log n）, 二分
        1。 寻找旋转点
        2。 二分查找 target
        """
        if not nums:
            return -1
        rotated_index = self._rotated_index(nums)
        size = len(nums)
        if rotated_index == 0:
            return self._search(nums, target, 0, size - 1)
        # target 在后面
        if target < nums[0]:
            return self._search(nums, target, rotated_index, size - 1)
        else:
            return self._search(nums, target, 0, rotated_index - 1)

    def _rotated_index(self, nums):
        left = 0
        right = len(nums) - 1
        # 数组未旋转
        if nums[left] < nums[right] or left == right:
            return 0
        while left < right:
            mid = (left + right) >> 1
            # 退出循环， 不能在while 结束后退出，否则 eg：
            # [4, 5, 6, 7, 0, 1, 2]
            # 第一次循环后， left=4， right=6， 最终返回 6
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            if nums[mid] < nums[left]:
                right = mid
            else:
                left = mid + 1
        # return left

    def _search(self, nums, target, left, right):
        while left < right:
            mid = (left + right) >> 1
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left if nums[left] == target else -1


if __name__ == '__main__':
    print(Solution().search([4, 5, 6, 7, 0, 1, 2], 0))
