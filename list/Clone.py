# -*- coding: utf-8 -*-
# 输入一个复杂链表（每个节点中有节点值，以及两个指针，
# 一个指向下一个节点，另一个特殊指针指向任意一个节点），
# 返回结果为复制后复杂链表的head。（
# 注意，输出结果中请不要返回参数中的节点引用，否则判题程序会直接返回空）


# 一、复制每个节点
# 当前节点 dummy
# 1.复制当前节点的下一个节点 dummy_next
# 2.复制当前节点值 copy_node
# 3.copy_node.next = dummy_next
# 4.dummy.next = copy_node
# 5.dummy = dummy_next
#
# 二、把复制节点的random指向被复制节点的random的下一个
# 1.dummy_random = dummy.random
# 2.被复制节点copy_node
# 3.copy_code.random = dummy_random.next
# 4.当前节点移到 dummy = copy_node.next
#
# 三、拆分新旧链表
# 1.被复制节点copy_node
# 2.copy_node的下一个节点dummy_next
# 3.原链表dummy.next = dummy_next
# 4.copy_node.next = dummy_next.next

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        if not pHead:
            return
        dummy = pHead
        while dummy:
            dummy_next = dummy.next
            # 新生成一个节点
            copy_node = RandomListNode(dummy.label)
            copy_node.next = dummy_next
            dummy.next = copy_node
            dummy = copy_node.next

        dummy = pHead
        while dummy:
            dummy_random = dummy.random
            copy_node = dummy.next
            if dummy_random:
                copy_node.random = dummy_random.next
            dummy = copy_node.next

        dummy = pHead
        copy_head = pHead.next
        while dummy:
            copy_node = dummy.next
            dummy_next = copy_node.next
            dummy.next = dummy_next
            if dummy_next:
                copy_node.next = dummy_next.next
            else:
                copy_node.next = None

            dummy = dummy_next

        return copy_head
