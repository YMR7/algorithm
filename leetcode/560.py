from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_dict = {}
        # num 直接等于 k
        sum_dict[0] = 1
        nums_sum = 0
        for num in nums:
            nums_sum += num
            other = nums_sum - k
            if other in sum_dict:
                count += sum_dict[other]
            # 更新字典值放最后：如果前 n - 3 的和为 k， 前 n 的和 也为 k，则 (n-3, n] 这一段的和也是 k,
            # 则 对于终点是 n 的数组有两个连续数组满足和为 k 的要求
            sum_dict[nums_sum] = sum_dict.get(nums_sum, 0) + 1
        return count

    def subarraySum2(self, nums: List[int], k: int) -> int:
        prefix_sum_li = []
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sum_li.append(prefix_sum)
        print(prefix_sum_li)
        count = 0
        size = len(prefix_sum_li)
        for i in range(size):
            if prefix_sum_li[i] == k:
                count += 1
            for j in range(i):
                if prefix_sum_li[i] - prefix_sum_li[j] == k:
                    print(i, j)
                    count += 1
        return count

    def subarraySum3(self, nums: List[int], k: int) -> int:
        # 初始化 0 位置值为 0，方便之后计算前 n 个数之和直接等于 k 的情况（即 j 等于 0）
        prefix_sum_li = [0]
        prefix_sum = 0
        for num in nums:
            prefix_sum += num
            prefix_sum_li.append(prefix_sum)
        print(prefix_sum_li)
        count = 0
        size = len(prefix_sum_li)
        for i in range(1, size):
            for j in range(i):
                if prefix_sum_li[i] - prefix_sum_li[j] == k:
                    print(i, j)
                    count += 1
        return count


res = Solution().subarraySum([1, 1, 3], 3)
print(res)
