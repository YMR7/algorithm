# 一个链表，奇数位升序偶数位降序，让链表变成升序

"""
1. 拆分为两个链表
2. 旋转链表
3. 合并
"""

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution:
    def test(self, root):
        odd = Node(-1)
        o = odd
        even = None
        pos = root
        i = 1
        while pos:
            tmp = pos.next
            if i % 2 != 0:
                pos.next = None
                o.next = pos
                o = o.next
            else:
                # 反转链表
                pos.next = even
                even = pos
            pos = tmp
            i += 1
        return self.merge(odd.next, even)

    def merge(self, head1, head2):
        """对两个链表进行归并，比较两个链表当中的值，合并到一个新的链表当中"""
        p1 = head1
        p2 = head2
        if head1.val < head2.val:
            head = head1
            p1 = p1.next
        else:
            head = head2
            p2 = p2.next

        p = head   # 新生成的头指针不能动, 由p来进行移动
        while p1 is not None and p2 is not None:
            if p1.val < p2.val:
                p.next = p1
                p1 = p1.next
                p = p.next
            else:
                p.next = p2
                p2 = p2.next
                p = p.next

        if p1 is not None:
            p.next = p1
        else:
            p.next = p2
        return head
    