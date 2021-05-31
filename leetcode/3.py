class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        size = len(s)
        windows = {}
        left = right = 0 
        max_len = 0
        while right < size:
            right_str = s[right]
            while right_str in windows:
                left_str = s[left]
                windows.pop(left_str)
                left += 1
            windows[right_str] = 1
            right += 1
            if right - left > max_len:
                max_len = right - left
        return max_len


if __name__ == '__main__':
    res = Solution().lengthOfLongestSubstring("abcabcbb")
    print(res)