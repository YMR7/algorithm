# -*- coding: utf-8 -*-
"""
给定一个字符串 s 和一些长度相同的单词 words。找出 s 中恰好可以由 words 中所有单词串联形成的子串的起始位置。

注意子串要与 words 中的单词完全匹配，中间不能有其他字符，但不需要考虑 words 中单词串联的顺序。

"""


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        # 1. 统计每个单词出现的次数
        # 2. 滑动窗口长度固定
        # 3. 对滑动窗口进行切分
        # 4. 统计切分后每个单词的出现次数
        if not s or not words:
            return []
        from collections import Counter
        one_word_length = len(words[0])
        sum_length = one_word_length * len(words)
        words = Counter(words)
        length_s = len(s)
        res = []
        for i in range(0, length_s - sum_length + 1):
            temp = s[i:i+sum_length]
            c_temp = []
            for j in range(0, sum_length, one_word_length):
                c_temp.append(temp[j:j+one_word_length])
            c_temp = Counter(c_temp)
            if c_temp == words:
                res.append(i)
                continue
        return res
