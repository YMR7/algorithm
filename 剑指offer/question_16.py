# 输入两个单调递增的链表，输出两个链表合成后的链表，
# 当然我们需要合成后的链表满足单调不减规则。

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        merge_list = ListNode(1)
        p = merge_list
        while pHead1 and pHead2:
            if pHead1.val >= pHead2.val:
                merge_list.next = pHead2
                pHead2 = pHead2.next
            else:
                merge_list.next = pHead1
                pHead1 = pHead1.next
            # 第一次循环后每次会覆盖掉后面的数
            merge_list = merge_list.next
        if pHead1:
            merge_list.next = pHead1
        if pHead2:
            merge_list.next = pHead2
        return p.next
