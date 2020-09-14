class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        """
        递归解法
        :param pre:
        :param tin:
        :return:
        """
        if not pre or not tin:
            return None
        head = pre[0]
        poi = tin.index(head)
        root = TreeNode(head)
        root.left = self.reConstructBinaryTree(pre[1:poi + 1], tin[:poi])
        root.right = self.reConstructBinaryTree(pre[poi + 1:], tin[poi + 1:])
        return root
