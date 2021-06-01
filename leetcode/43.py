class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        size_1 = len(num1)
        size_2 = len(num2)
        res = ['0'] * (size_1 + size_2)
        for i in range(size_1 - 1, -1, -1):
            for j in range(size_2 - 1, -1, -1):
                multi = int(num1[i]) * int(num2[j])
                left = i + j
                right = i + j + 1
                carry = multi + int(res[right])
                res[left] = str(carry // 10 + int(res[left]))
                res[right] = str(carry % 10)
        count = 0
        for num in res:
            if num == '0':
                count += 1
            else:
                break
        
        return '0' if count == (size_1 + size_2) else ''.join(res[count:])


res = Solution().multiply("123", "456")
print(res)