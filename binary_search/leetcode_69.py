class Solution:
    def mySqrt(self, x: int) -> int:
        left = 0
        right = x // 2 + 1
        while left < right:
            # 右中位数, 只有两个数时中位数是右边，右边排除（减一）
            mid = (left + right + 1) >> 1
            if mid ** 2 > x:
                right = mid - 1
            else:
                left = mid
        return left


# 牛顿法
"""
class Solution:

    def mySqrt(self, x):
        if x < 0:
            raise Exception('不能输入负数')
        if x == 0:
            return 0
        # 起始的时候在 1 ，这可以比较随意设置
        cur = 1
        while True:
            pre = cur
            cur = (cur + x / cur) / 2
            if abs(cur - pre) < 1e-6:
                return int(cur)


"""

if __name__ == '__main__':
    print(Solution().mySqrt(8))
