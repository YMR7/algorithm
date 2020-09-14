class Solution:
    def Power(self, base, exponent):
        # write code here
        """
        快速幂算法，需要注意的是 指数为奇数时会少乘一次
        :param base:
        :param exponent:
        :return:
        """
        if base == 0:
            return 0

        if exponent == 0:
            return 1

        e = abs(exponent)

        # 演示
        # if e % 2 == 0:
        #     while e > 1:
        #         base = base * base
        #         e = e >> 1
        # else:
        #     temp = base
        #     while e > 1:
        #         base = base * base
        #         e = e >> 1
        #     base = base * temp
        # return base if exponent > 0 else 1 / base

        res = 1
        temp = base
        while e > 0:
            # 如果 exponent 是偶数， 会在最后执行一次；如果是奇数， 相比偶数会多运行一次乘法
            if e % 2 == 1:
                res = res * temp
            temp *= temp
            e = e >> 1
        return res if exponent > 0 else 1 / res


if __name__ == '__main__':
    print(Solution().Power(2, 4))
