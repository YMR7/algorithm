"""
Given an unsorted array of integers, find the length of longest increasing subsequence.

Example:

Input: [10,9,2,5,3,7,101,18]
Output: 4
Explanation: The longest increasing subsequence is [2,3,7,101], therefore the length is 4.
Note:

There may be more than one LIS combination, it is only necessary for you to return the length.
Your algorithm should run in O(n2) complexity.
Follow up: Could you improve it to O(n log n) time complexity?

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/longest-increasing-subsequence
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        """
        时间复杂度是O （nlogn）
        完整遍历一次数组，每次遍历需要用到二分

        tail 里面存储的数不一定是最长上升序列的数，但tail长度是题目要求的结果
        """
        if not nums or len(nums) == 0:
            return 0
        tail = []
        for num in nums:
            left = 0
            # 可能是在末尾追加num， 所以不要 减 1
            right = len(tail)
            while left < right:
                mid = (left + right) >> 1
                # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                if tail[mid] < num:
                    left = mid + 1
                else:
                    right = mid
            if left == len(tail):
                tail.append(num)
            else:
                tail[left] = num
        return len(tail)


if __name__ == '__main__':
    print(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))
