class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self) -> None:
        self.head = None
        self.pre = None

    def treeToDoublyList(self, root: "Node") -> "Node":
        if not root:
            return
        self.dfs(root)
        self.head.left = self.pre
        self.pre.right = self.head
        return self.head

    def dfs(self, cur):
        if not cur:
            return
        self.dfs(cur.left)
        if self.pre:
            self.pre.right = cur
            cur.left = self.pre
        else:
            # 头节点
            self.head = cur
        self.pre = cur
        self.dfs(cur.right)
