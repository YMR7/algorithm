# 输入两个链表，找出它们的第一个公共结点。

"""
1. 有公共节点说明链表是 y 字形
2. 获取两个链表的长度a， b，长链表先走 abs(a-b) 步
3. 两个链表同时走
"""
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1 = pHead1
        p2 = pHead2
        lenght1 = lenght2 = 0

        while p1:
            lenght1 += 1
            p1 = p1.next
        while p2:
            lenght2 += 1
            p2 = p2.next
        if lenght1 < lenght2:
            pHead1, pHead2 = pHead2, pHead1
        distance = abs(lenght1 - lenght2)
        for i in range(distance):
            pHead1 = pHead1.next
        while pHead1 != pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1
