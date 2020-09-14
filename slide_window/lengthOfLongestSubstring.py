"""
给定一个字符串，找出不含有重复字符的最长子串的长度。
"""

# 从左边一直删除到重复元素位置
class Solution:
    def lengthOfLongestSubstring(self, s):
        size = len(s)
        max_length = 0
        cur_length = 0
        left = 0
        window = set()
        for i in range(size):
            while s[i] in window:
                # set 无序，从 s 的左边开始移除 set 里面对应的字符
                window.remove(s[left])
                left += 1
                cur_length -= 1
            # s[i] 一定会加到window中
            cur_length += 1
            window.add(s[i])
            if cur_length > max_length:
                max_length = cur_length
        return max_length

