class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = end = 0
        for i in range(len(s)):
            # 对称点是某个字母
            len1 = self.test(s, i, i)
            # 对称点在两个字母间
            len2 = self.test(s, i, i + 1)
            max_len = max(len1, len2)
            if max_len > end - start:
                start = i - (max_len - 1) // 2
                end = i + max_len // 2
        return s[start:end + 1]

    def test(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # 减一是因为最后一次不满足条件
        return right - left - 1


if __name__ == "__main__":
    res = Solution().longestPalindrome('babad')
    print(res)
