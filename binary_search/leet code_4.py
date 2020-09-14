# 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
#
# 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
#
# 你可以假设 nums1 和 nums2 不会同时为空。
#
# 示例 1:
#
# nums1 = [1, 3]
# nums2 = [2]
#
# 则中位数是 2.0
# 示例 2:
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# 则中位数是 (2 + 3)/2 = 2.5
#
"""
二分搜索小技巧
- 循环条件 while left < right
- 考虑只有两个元素时是否会出现死循环
    - 两个分支，一个排除中位数，一个不排除
- 根据最后循环退出时的值是否在[left, right] 这个区间再再考虑是否还要判断
"""

"""
判断 数 n 是奇数还是偶数
奇数： n & 1 == 1
偶数： n $ 1 == 0

设数组1长度n， 数组2长度m
寻找两个数组中第 k 小的问题
a 中找到位置i，b中找到位置j，i+j=k(i, j从1开始计数,0 代表数组为空)
则有 a[i-1] <= b[j] && b[j-1]<=a[i]
第 k 小为 max(a[i-1], b[j-1])

0 <= i <= n
0 <= j <= m    ==> max(0, k-m) <= i <= min(k, n)  
i + j = k
k-m <= i <= k

"""
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        assert n > 0 or m > 0
        size = m + n
        if size & 1:
            # 奇数
            return self.binary_search(nums1, nums2, (size >> 1) + 1)
        else:
            # 偶数
            # >> 优先级小于 +
            return (self.binary_search(nums1, nums2, size >> 1) + self.binary_search(nums1, nums2, (size >> 1) + 1)) / 2

    def binary_search(self, nums1, nums2, k):
        n = len(nums1)
        m = len(nums2)
        left = max(0, k - m)
        right = min(k, n)
        while left < right:

            """
            此处不理解， 为什么在这种情况下是 left = mid + 1?
            
            极端情况下 nums1 为 null， 此时 n = 0, left = 0, right = 0, 不进入 while 循环
            
            nums1 = [2, 4 ,7, 9, 11]
            nums2 = [3, 5, 6, 8, 10, 15, 17, 19]
            
            n = 5, m = 8, k = 7
            left = max(0, k - m) = 0
            right = min(k, m) = 7
            
            第一次循环：
                mid  = 3
                nums2[k-mid-1] = muns2[3] = 8
                nums1[mid] = nums1[3] = 9 
                此时：
                nums2[k-mid-1] < nums1[mid]
                right = mid = 3
            第二次循环：
                left = 0
                right = 3
                mid = 1
                
                nums2[k-mid-1] = nums2[5] = 15
                nums1[mid] = nums1[1] = 4
                
                nums2[k-mid-1] > nums1[mid]
                left = mid + 1 = 2
            第三次循环：
                left = 2
                right = 3
                mid = 2
                
                nums2[k-mid-1] = nums2[4] = 10
                nums1[mid] = nums1[2] = 7
                nums2[k-mid-1] > nums1[mid]
                left = mid + 1 = 3 
            注意点：
                1. (k - mid - 1) + mid   ==   k - 1, 相加为 k-1
            """
            mid = (left + right) >> 1
            if nums2[k - mid - 1] > nums1[mid]:
                left = mid + 1
            else:
                right = mid
        if left == 0:
            return nums2[k - 1]
        elif left == k:
            return nums1[k - 1]
        return max(nums1[left - 1], nums2[k - left - 1])


if __name__ == '__main__':
    print(Solution().findMedianSortedArrays([1, 2], [3, 4, 5, 6]))
