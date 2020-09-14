# 二叉树的公共祖先


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


"""
递归实现
1. 从根节点开始遍历树。
2. 如果当前节点本身是 p 或 q 中的一个，我们会将变量 mid 标记为 true，并继续搜索左右分支中的另一个节点。
3. 如果左分支或右分支中的任何一个返回 true，则表示在下面找到了两个节点中的一个。
4. 如果在遍历的任何点上，左、右或中三个标志中的任意两个变为 true，这意味着我们找到了节点 p 和 q 的最近公共祖先。

"""

class Solution1:

    def __init__(self):
        # Variable to store LCA node.
        self.ans = None

    def lowestCommonAncestor(self, root, p, q):

        def recurse_tree(current_node):
            if not current_node:
                return False
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
            mid = current_node == p or current_node == q

            # If any two of the three flags left, right or mid become True.
            if mid + left + right >= 2:
                self.ans = current_node

            return mid or left or right
        recurse_tree(root)
        return self.ans


"""
非递归实现
1. 分别找到 root 到 p、q的路径
"""

class Solution2:
    def lowestCommonAncestor(self, root, p, q):

        queue = []
        queue.append([[root], root])
        result = []

        while len(queue) != 0:
            cur_path = queue[0][0]
            cur_node = queue[0][1]
            queue.pop(0)
            if cur_node.val == p.val or cur_node.val == q.val:
                result.append(cur_path)
                if len(result) == 2:
                    break

            if cur_node.left != None:
                left_path = cur_path[:]
                left_path.append(cur_node.left)
                queue.append([left_path, cur_node.left])
            if cur_node.right != None:
                right_path = cur_path[:]
                right_path.append(cur_node.right)
                queue.append([right_path, cur_node.right])

        i = 0
        while i < min(len(result[0]), len(result[1])):
            if result[0][i].val != result[1][i].val:
                break
            i += 1
        return result[0][i - 1]


# 二叉搜索树的公共祖先
"""
递归

1. 从根节点开始遍历树
2. 如果节点 pp 和节点 qq 都在右子树上，那么以右孩子为根节点继续 1 的操作
3. 如果节点 pp 和节点 qq 都在左子树上，那么以左孩子为根节点继续 1 的操作
4. 如果条件 2 和条件 3 都不成立，这就意味着我们已经找到节 pp 和节点 qq 的 LCA 了
"""

class Solution3:
    def lowestCommonAncestor(self, root, p, q):

        parent_val = root.val
        p_val = p.val
        q_val = q.val

        if p_val > parent_val and q_val > parent_val:
            return self.lowestCommonAncestor(root.right, p, q)
        elif p_val < parent_val and q_val < parent_val:
            return self.lowestCommonAncestor(root.left, p, q)
        else:
            return root


"""
非递归（用迭代）
找到分割点：分割点就是能让节点 p 和节点 q 不能在同一颗子树上的那个节点，
或者是节点 p 和节点 q 中的一个，这种情况下其中一个节点是另一个节点的祖先

"""
class Solution4:
    def lowestCommonAncestor(self, root, p, q):
        p_val = p.val
        q_val = q.val
        node = root
        while node:
            parent_val = node.val
            if p_val > parent_val and q_val > parent_val:
                node = node.right
            elif p_val < parent_val and q_val < parent_val:
                node = node.left
            else:
                return node
