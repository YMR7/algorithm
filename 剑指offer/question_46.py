class Solution:
    def translateNum(self, num: int) -> int:
        offest_one = 1
        offest_two = 1
        pre_mod = num % 10
        while num:
            num //= 10
            cur_mod = num % 10
            if 10 <= cur_mod * 10 + pre_mod <= 25:
                offest_zero = offest_one + offest_two
            else:
                offest_zero = offest_one
            offest_two = offest_one
            offest_one = offest_zero
            pre_mod = cur_mod
        return offest_one


ans = Solution().translateNum(12258)
print(ans)