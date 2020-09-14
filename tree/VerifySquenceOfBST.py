# -*- coding:utf-8 -*-
# 输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历的结果。
# 如果是则输出Yes,否则输出No。假设输入的数组的任意两个数字都互不相同。
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return
        length = len(sequence)
        if length == 1:
            return True
        root = sequence[-1]
        i = 0
        while sequence[i] < root:
            i += 1
        for j in range(i, length):
            if sequence[j] < root:
                return False
        left_tree = True
        right_tree = True
        if sequence[:i]:
            left_tree = self.VerifySquenceOfBST(sequence[:i])
        if sequence[i:length-1]:
            right_tree = self.VerifySquenceOfBST(sequence[i:length-1])
        return left_tree and right_tree
