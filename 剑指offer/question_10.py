class Solution:
    def rectCover(self, number):
        # write code here
        # 数学归纳法
        if number <= 1:
            return number
        a = 1
        b = 2
        for _ in range(number-1):
            temp = b
            b = a + b
            a = temp
        return a