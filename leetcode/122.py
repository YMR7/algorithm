from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        size = len(prices)
        if size <= 1:
            return 0
        res = 0
        pre = prices[0]
        for num in prices[1:]:
            if num > pre:
                res = res + (num - pre)
            pre = num
        return res


ans = Solution().maxProfit([7, 1, 5, 3, 6, 4])
print(ans)
