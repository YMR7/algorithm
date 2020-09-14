# -*- coding: utf-8 -*-
# 写一个函数，求两个整数之和，要求在函数体内不得使用+、-、*、/四则运算符号。


class Solution:
    def Add(self, num1, num2):
        # write code here
        # num2 可以小于0
        while num2:
            carry = ((num1 & num2) << 1) & 0xffffffff
            num1 = (num1 ^ num2) & 0xffffffff

            num2 = carry
        return num1 if num1 <= 0x7fffffff else ~(num1 ^ 0xffffffff)