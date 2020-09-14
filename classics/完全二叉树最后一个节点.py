# 完全二叉树寻找最后一行的最后一个节点
"""

首先遍历完全二叉树的左分支，求出完全二叉树的高度depth, 
然后对于每个子树的根节点，先从根节点的右孩子开始，
然后从此节点遍历该节点的左孩子，等遍历完成后，
进行判断此时临时高度等于二叉树的高度，且节点无右孩子时候，则输出该节点，
否则右侧还有节点，则遍历右子树，若临时高度小于二叉树的高度，则遍历根节点的左孩子。

"""
class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def printlastnode(self, root):
        if not root:
            return None

        depth = 0
        tmp = root
        # 首先先计算二叉树的高度
        while tmp:
            depth += 1
            tmp = tmp.left

        level = 0
        tempdepth = 0

        # 遍历二叉树
        while root:
            level += 1
            if level == depth:
                break

            curnode = root

            # 先遍历右孩子，若无右孩子，则玩根节点的左孩子遍历
            if curnode.right:
                parent = curnode
                curnode = curnode.right

                # 设置临时高度
                tempdepth = level + 1

                # 然后循环往左孩子遍历
                while curnode.left:
                    tempdepth = tempdepth + 1
                    parent = curnode
                    curnode = curnode.left

                # 若临时统计高度小于二叉树高度，则往根节点的左孩子遍历
                if tempdepth < depth:
                    root = root.left

                # 若当前节点无右孩子，且高度等于二叉树高度，则输出当前节点
                elif not curnode.right or parent.right == curnode:
                    return curnode
                else:
                    root = root.right

            else:
                root = root.left

        return root

