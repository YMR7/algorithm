class Solution:
    def jumpFloorII(self, number):
        # write code here
        # 数学归纳法
        if number <= 1:
            return number
        return 1 << (number-1)


if __name__ == '__main__':
    print(Solution().jumpFloorII(3))