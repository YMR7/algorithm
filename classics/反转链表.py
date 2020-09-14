# 输入一个链表，反转链表后，输出新链表的表头。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        last = None
        while pHead:
            temp = pHead.next
            pHead.next = last
            last = pHead
            pHead = temp
        return last


# 反转从位置 m 到 n 的链表
class Solution:
    def reverseBetween(self, head, m, n):
        if m == n:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        a, d = dummy, dummy
        # a 是 m 前一个节点
        for _ in range(m - 1):
            a = a.next
        # d 是 n 节点
        for _ in range(n):
            d = d.next
        b, c = a.next, d.next
        pre = b
        cur = pre.next
        # 反转 m 到 n
        while cur != c:
            next = cur.next
            cur.next = pre
            pre = cur
            cur = next
        a.next = d
        b.next = c
        return dummy.next
