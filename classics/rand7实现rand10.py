"""
已有方法 rand7 可生成 1 到 7 范围内的均匀随机整数，试写一个方法 rand10 生成 1 到 10 范围内的均匀随机整数。

不要使用系统的 Math.random() 方法。

"""
import random


def rand7():
    return random.randrange(1, 7)


class Solution:


    def rand10(self):
        """
        :rtype: int
        """
        while True:
            row = rand7()
            col = rand7()
            num = col + (row - 1) * 7
            if num <= 40:
                break
        return 1 + (num - 1) % 10 # 1-10
