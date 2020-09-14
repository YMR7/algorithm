# -*- coding: utf-8 -*-
# 请设计一个算法，给一个字符串进行二进制编码，使得编码后字符串的长度最短。

class Huffman(object):
    def __init__(self, strs):
        self.strs = strs
        self.char_rate = {}

    def get_char_rate(self):
        for char in self.strs:
            if char in self.char_rate:
                self.char_rate[char] += 1
            else:
                self.char_rate.setdefault(char, 1)

        self.char_rate = sorted(self.char_rate.items(), key=lambda x: x[1])

