# 给定一个字符串，请你找出其中不含有重复字符的 最长子串 的长度。

"""
滑动窗口
"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        max_length = 0
        cur_length = 0
        left = 0
        window = set()
        for i in range(size):
            # 从左边一直删除到重复元素位置
            while s[i] in window:
                window.remove(s[left])
                left += 1
                cur_length -= 1
            # s[i] 一定会加到window中
            cur_length += 1
            window.add(s[i])
            if cur_length > max_length:
                max_length = cur_length
        return max_length
