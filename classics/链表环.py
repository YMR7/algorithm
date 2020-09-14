# 给一个链表，若其中包含环，请找出该链表的环的入口结点，否则，输出null。


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def EntryNodeOfLoop(self, pHead):
        if not pHead:
            return
            # write code here
        fast = pHead
        slow = pHead
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                while slow != pHead:
                    slow = slow.next
                    pHead = pHead.next
                return slow
        return