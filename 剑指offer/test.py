# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        li_1 = [root]
        res = []
        while li_1:
            temp = li_1.pop(0)
            if temp:
                li_1.append(temp.left)
                li_1.append(temp.right)
                res.append(str(temp.val))
            else:
                res.append('null')
        return '[' + ','.join(res) + ']'

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return
        data = data[1:-1].split(',')
        root = TreeNode(int(data.pop(0)))
        li = [root]
        while data:
            node = li.pop(0)
            left = data.pop(0)
            if left != 'null':
                node_left = TreeNode(int(left))
                node.left = node_left
                li.append(node_left)
            right = data.pop(0)
            if right != 'null':
                node_right = TreeNode(int(right))
                node.right = node_right
                li.append(node_right)
        return root


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


if __name__ == "__main__":
    codec = Codec()
    res = codec.deserialize('[1,2,3,null,null,4,5]')
    print(res)
