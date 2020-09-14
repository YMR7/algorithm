# -*- coding: utf-8 -*-
"""
给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字母的最小子串。

示例：

输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
说明：

如果 S 中不存这样的子串，则返回空字符串 ""。
如果 S 中存在这样的子串，我们保证它是唯一的答案。

"""

from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # 1. 从左往右找到包含T的子串
        # 2. 从左往右移出字符，直到不满足要求
        # 3. 右指针继续往右移到，直到找到包含T的子串，循环2,3
        if not s or not t:
            return ''
        left, right = 0, 0
        t_dict = Counter(t)
        length = len(t_dict)
        formed = 0
        ans = (float('inf'), None, None)
        slide_window = {}
        while right < len(s):
            char = s[right]
            slide_window[char] = slide_window.get(char, 0) + 1
            if char in t_dict and t_dict[char] == slide_window[char]:
                formed += 1
            while left <= right and formed == length:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right-left+1, left, right)
                slide_window[char] -= 1
                if char in t_dict and slide_window[char] < t_dict[char]:
                    formed -= 1
                left += 1
            right += 1

        return '' if ans[0] == float('inf') else s[ans[1]:ans[2]+1]



