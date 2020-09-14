# -*- coding: utf-8 -*-


class TreeNode:
    def __init__(self, data):
        self.val = data
        self.l_child = None
        self.r_child = None


def create_tree(nums):
    if not nums:
        return
    length = len(nums)
    head = TreeNode(nums[0])

    if length == 1:
        return head

    count = 1
    temp = [head]
    for node in temp:
        # '#'代表None
        if node != '#':
            node.l_child = TreeNode(nums[count])
            temp.append(node.l_child)
            count += 1
            if count == length:
                return head
            node.r_child = TreeNode(nums[count])
            temp.append(node.r_child)
            count += 1
            if count == length:
                return head
    return head


if __name__ == '__main__':
    # '#'代表None
    nodes = [1, 2, 3, 4, '#']
    root = create_tree(nodes)
