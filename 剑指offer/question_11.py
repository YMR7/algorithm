class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        # 负数时取后32位
        n = n & 0xffffffff
        while n != 0:
            n = (n - 1) & n
            count += 1
        return count


if __name__ == '__main__':
    print(Solution().NumberOf1(10))
    # aa = -1
    # print(aa >> 1)
    # print(bin(aa))
