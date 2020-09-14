class Solution:
    def Fibonacci(self, n):
        # write code here

        # # 递归
        # if n <= 1:
        #     return n
        # return self.Fibonacci(n-1) + self.Fibonacci(n-2)

        if n <= 1:
            return n
        a = 0
        b = 1
        for i in range(n):
            temp = b
            b = a + b
            a = temp
        return a


if __name__ == '__main__':
    print(Solution().Fibonacci(4))