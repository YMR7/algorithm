# -*- coding: utf-8 -*-
# 输入一棵二叉搜索树，将该二叉搜索树转换成
# 一个排序的双向链表。要求不能创建任何新的结点，只能调整树中结点指针的指向。


# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:

    def Convert(self, pRootOfTree):

        if not pRootOfTree:
            return
        self.arr = []
        self.inorder_traversal(pRootOfTree)
        for index, node in enumerate(self.arr[:-1]):
            # 最大node的right为None
            node.right = self.arr[index+1]
            # 最小node的left为None
            self.arr[index+1].left = node
        return self.arr[0]

    def inorder_traversal(self, root):
        if not root:
            return
        if root.left:
            self.inorder_traversal(root.left)
        self.arr.append(root)
        if root.right:
            self.inorder_traversal(root.right)
