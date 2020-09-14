# 输入一颗二叉树的根节点和一个整数，打印出二叉树中结点值的和为输入整数的所有路径。
# 路径定义为从树的根结点开始往下一直到叶结点所经过的结点形成一条路径。
# (注意: 在返回值的list中，数组长度大的数组靠前)
#


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        if not root:
            return []
        res = []
        def find_path_main(root, path, current_sum):
            current_sum += root.val
            path.append(root)
            # 叶子节点
            is_leaf = root.left is None and root.right is None
            if is_leaf and current_sum == expectNumber:
                one_path = []
                for node in path:
                    one_path.append(node.val)
                res.append(one_path)
            if current_sum < expectNumber:
                if root.left:
                    find_path_main(root.left, path, current_sum)
                if root.right:
                    find_path_main(root.right, path, current_sum)
            path.pop()
        find_path_main(root, [], 0)
        return sorted(res, reverse=False)