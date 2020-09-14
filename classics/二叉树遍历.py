# 先序

#  先压入右孩子，再左孩子
def preOrderTravese(node):
    stack = [node]
    while len(stack) > 0:
        node = stack.pop()
        print(node.val)
        if node.right is not None:
            stack.append(node.right)
        if node.left is not None:
            stack.append(node.left)


# - 中序
# 从根节点开始，左节点不断入栈，左节点为空时出栈一个节点，
# 出栈节点的右节点的左节点不断入栈
def inOrderTraverse(node):
    stack = []
    pos = node
    while pos is not None or len(stack) > 0:
        if pos is not None:
            stack.append(pos)
            pos = pos.left
        else:
            pos = stack.pop()
            print(pos.val)
            pos = pos.right


# - 后序

# 后序打印二叉树（非递归）
# 使用两个栈结构
# 第一个栈进栈顺序：左节点->右节点->根节点(最开始没有左右节点，根节点先入栈)
# 第一个栈弹出顺序： 根节点->右节点->左节点(先序遍历栈弹出顺序：根->左->右)
# 第二个栈存储为第一个栈的每个弹出依次进栈
# 最后第二个栈依次出栈
def postOrderTraverse(node):
    stack = [node]
    stack2 = []
    while len(stack) > 0:
        node = stack.pop()
        stack2.append(node)
        if node.left is not None:
            stack.append(node.left)
        if node.right is not None:
            stack.append(node.right)
    while len(stack2) > 0:
        print(stack2.pop().val)



# 层序（广度优先遍历）

# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution4:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        if not root:
            return []
        nodes = []
        bfs_nodes = []
        nodes.append(root)
        while nodes:
            node = nodes.pop(0)
            bfs_nodes.append(node.val)
            if node.left:
                nodes.append(node.left)
            if node.right:
                nodes.append(node.right)
        return bfs_nodes

