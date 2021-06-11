class Solution:
    def test(self, n: int) -> int:
        if n < 10:
            return n
        count = 1
        n -= 9
        while True:
            num = 10 ** count * 9 * (count + 1)
            if n > num:
                n -= num
                count += 1
            else:
                i, j = divmod(n, count + 1)
                if j:
                    temp = str(10 ** count + i)
                    return int(temp[j - 1])
                else:
                    temp = str(10 ** count + i - 1)
                    return int(temp[-1])

ans = Solution().test(11)
print(ans)