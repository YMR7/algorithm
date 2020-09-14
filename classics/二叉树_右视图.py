# 给定一棵二叉树，想象自己站在它的右侧，按照从顶部到
# 底部的顺序，返回从右侧所能看到的节点值。


"""
深度优先搜索, 总是先访问右子树,
保证访问树的某个特定深度时，正在访问的节点总是该深度的最右侧节点
 时间复杂度: O(n), 空间复杂度: O(n)
"""
class Solution1(object):
    def rightSideView(self, root):
        # depth -> node.val
        dict_data = dict() 
        max_depth = -1

        stack = [(root, 0)]
        while stack:
            node, depth = stack.pop()

            if node is not None:
                # maintain knowledge of the number of levels in the tree.
                max_depth = max(max_depth, depth)
                # only insert into dict if depth is not already present.
                dict_data.setdefault(depth, node.val)

                stack.append((node.left, depth+1))
                stack.append((node.right, depth+1))

        return [dict_data[depth] for depth in range(max_depth+1)]



"""
广度优先搜索, 不断更新同一深度最右节点的值
"""
from collections import deque


class Solution(object):
    def rightSideView(self, root):
        dict_data = dict()
        max_depth = -1

        queue = deque([(root, 0)])
        while queue:
            node, depth = queue.popleft()

            if node is not None:
                max_depth = max(max_depth, depth)
                dict_data[depth] = node.val

                queue.append((node.left, depth+1))
                queue.append((node.right, depth+1))

        return [dict_data[depth] for depth in range(max_depth+1)]
