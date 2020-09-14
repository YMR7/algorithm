class Solution:
    def jumpFloor(self, number):
        # write code here
        # 统计归纳法
        if number <= 1:
            return number
        a = 0
        b = 1
        for _ in range(number+1):
            temp = b
            b = a + b
            a = temp
        return a