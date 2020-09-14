# -*- coding: utf-8 -*-
# 输入一棵二叉树，判断该二叉树是否是平衡二叉树。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def IsBalanced_Solution(self, pRoot):
        # write code here
        return self.get_depth(pRoot) != -1

    def get_depth(self, node):
        if node is None:
            return 0
        # -1 即不平衡
        left = self.get_depth(node.left)
        if left == -1:
            return -1
        right = self.get_depth(node.right)
        if right == -1:
            return -1
        if abs(left - right) > 1:
            return -1
        return max(left, right) + 1
