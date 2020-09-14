class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


"""
给出两个 非空 的链表用来表示两个非负的整数。
其中，它们各自的位数是按照 逆序 的方式存储的，
并且它们的每个节点只能存储 一位 数字。
如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

"""


class Solution:
    def addTwoNumbers(self, l1, l2):
        head = ListNode(0)  #头结点，无存储，指向链表第一个结点
        node = head         #初始化链表结点
        carry = 0           #初始化 进一 的数
        while l1 or l2:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            sum = x + y + carry              # 对每一位求和
            carry = sum // 10                # 地板除，求进一（其为0或1）
            node.next = ListNode(sum % 10)   # 取余数，求本位结点
            if l1:                           # 求空否，防止出现无后继结点
                l1 = l1.next
            if l2:                           # 同上
                l2 = l2.next
            node = node.next                 # 更新指针
        if carry != 0:                       # 验证最后一位相加是否需 进一
            node.next = ListNode(1)
        return head.next



"""
给定两个非空链表来代表两个非负整数。数字最高位位于链表开始位置。
它们的每个节点只存储单个数字。将这两数相加会返回一个新的链表。
你可以假设除了数字 0 之外，这两个数字都不会以零开头。
进阶:
如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。
"""


# 借用栈，压入栈中，按栈顶元素相加
class Solution2:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        stack1 = []
        stack2 = []
        dummy = ListNode(-1)

        def push_stack(p, stack):
            while p:
                stack.append(p.val)
                p = p.next

        push_stack(l1, stack1)
        push_stack(l2, stack2)
        # 记录进位
        carry = 0
        while stack1 or stack2 or carry:
            tmp1, tmp2 = 0, 0
            if stack1:
                tmp1 = stack1.pop()
            if stack2:
                tmp2 = stack2.pop()
            carry, mod = divmod(tmp1 + tmp2 + carry, 10)
            # 头插法
            new_node = ListNode(mod)
            new_node.next = dummy.next
            dummy.next = new_node
        return dummy.next
