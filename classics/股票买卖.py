# 股票的最大利润
# 假设把某股票的价格按照时间先后顺序存储在数组中，
# 请问买卖该股票一次可能获得的最大利润是多少？


"""
1. 前i日最大利润=max(前(i−1)日最大利润,第i日价格−前i日最低价格)
2. 变量（记为成本 cost ）每日更新最低价格
"""

class Solution1:
    def maxProfit(self, prices):
        cost, profit = float("+inf"), 0
        for price in prices:
            cost = min(cost, price)
            profit = max(profit, price - cost)
        return profit


# 可以多次买卖一支股票
"""
贪心
"""
class Solution2:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            tmp = prices[i] - prices[i - 1]
            if tmp > 0:
                profit += tmp
        return profit

# 买卖两次
"""
找出分割点
"""
class Solution3:
    def maxProfit(self, prices):
        size = len(prices)
        if size < 2:
            return 0

        # [0, left] 区间里进行一次买卖的最大收益
        left = [0 for _ in range(size)]
        min_val = prices[0]

        for i in range(1, size):
            left[i] = max(left[i - 1], prices[i] - min_val)
            min_val = min(min_val, prices[i])

        # [right, len - 1] 区间里进行一次买卖的最大收益
        right = [0 for _ in range(size)]
        max_val = prices[size - 1]

        for i in range(size - 2, -1, -1):
            right[i] = max(right[i + 1], max_val - prices[i])
            max_val = max(max_val, prices[i])
        #  这里有一个坑，有可能是只交易一次的场景
        res = max(left[size - 1], right[0])
        for i in range(1, size - 2):
            res = max(res, left[i] + right[i + 1])
        return res

