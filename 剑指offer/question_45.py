from typing import List


class Solution:
    def minNumber(self, nums: List[int]) -> str:
        nums = list(map(str, nums))
        size = len(nums)
        self.quick_sort(nums, 0, size - 1)
        return ''.join(nums)

    def quick_sort(self, nums, left, right):
        if left >= right:
            return
        i = left
        j = right
        temp = nums[left]
        while i < j:
            # 必须从右边开始
            # temp < nums[j]
            while temp + nums[j] <= nums[j] + temp and i < j:
                j -= 1
            # temp > nums[i]
            while temp + nums[i] >= nums[i] + temp and i < j:
                i += 1
            nums[i], nums[j] = nums[j], nums[i]
        nums[left], nums[i] = nums[i], nums[left]
        self.quick_sort(nums, i + 1, right)
        self.quick_sort(nums, left, i - 1)


if __name__ == '__main__':
    res = Solution().minNumber([10, 2])
    print(res)