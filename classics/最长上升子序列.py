# 给定一个无序的整数数组，找到其中最长上升子序列的长度。


"""
# 动态规划
dp[i] 的值代表 nums 前 ii 个数字的最长子序列长度

"""
class Solution:
    def lengthOfLIS(self, nums) -> int:
        if not nums: return 0
        # 含义是每个元素都至少可以单独成为子序列，此时长度都为1
        dp = [1] * len(nums)
        for i in range(len(nums)):
            for j in range(i):
                if nums[j] < nums[i]: # 如果要求非严格递增，将此行 '<' 改为 '<=' 即可。
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)


class Solution2:
    def lengthOfLIS(self, nums) -> int:
        """
        时间复杂度是O （nlogn）
        完整遍历一次数组，每次遍历需要用到二分

        tail 里面存储的数不一定是最长上升序列的数，但tail长度是题目要求的结果
        tail[i] 保存遍历过程中长度为i+1的最长上升子序列的最小尾元素
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
