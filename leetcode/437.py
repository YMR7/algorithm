# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if not root:
            return 0
        # 以此节点为路径起点的满足条件数
        path_head = self.count(root, targetSum)
        # 以左节点为路径起点的满足条件数
        path_left = self.pathSum(root.left, targetSum)
        # 以右节点为路径起点的满足条件数
        path_right = self.pathSum(root.right, targetSum)
        return path_head + path_left + path_right

    def count(self, head, target):
        if not head:
            return 0
        # 当前节点是否满足条件
        is_me = 1 if head.val == target else 0
        # 即使当前节点已经满足条件，后面可能会出现， -1， 1 这样的路径
        # 又满足条件
        left = self.count(head.left, target - head.val)
        right = self.count(head.right, target - head.val)
        return is_me + left + right