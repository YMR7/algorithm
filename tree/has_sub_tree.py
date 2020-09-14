# -*- coding:utf-8 -*-
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# 输入两棵二叉树A，B，判断B是不是A的子结构。（ps：我们约定空树不是任意一个树的子结构）
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        if pRoot1 == None or pRoot2 == None:
            return False
        flag = False
        # 根节点,调用if_tree1_has_tree2
        if pRoot1.val == pRoot2.val:
            flag = self.if_tree1_has_tree2(pRoot1, pRoot2)
        # 左节点,调用本身
        if not flag:
            flag = self.HasSubtree(pRoot1.left, pRoot2)
        # 右节点,调用本身
        if not flag:
            flag = self.HasSubtree(pRoot1.right, pRoot2)
        return flag

    def if_tree1_has_tree2(self, tree1, tree2):
        if not tree2:
            return True
        if not tree1:
            return False
        if tree1.val != tree2.val:
            return False
        return self.if_tree1_has_tree2(tree1.left, tree2.left) and self.if_tree1_has_tree2(tree1.right, tree2.right)
