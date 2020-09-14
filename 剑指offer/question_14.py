class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class CreateListNode:
    def __init__(self):
        self.root = None

    def create(self, arrays):
        for num in arrays:
            node = ListNode(num)
            if self.root is None:
                self.root = node
                temp = self.root
            else:
                temp.next = node
                temp = temp.next
        return self.root


class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        # assert k > 0, 'k lower 0'
        if k <= 0 or not head:
            return {}
        temp = ListNode(None)
        res = temp
        while head:
            if k > 0:
                k -= 1
            else:
                res = res.next
            tail = head
            temp.next = tail
            temp = temp.next
            # 预先把下一个节点的地址赋值给变量
            head = head.next
            # 必须放在head赋值语句之后，不然head会指向None
            temp.next = None
        return res.next if k == 0 else {}


#  链表赋值问题
#  是引用，使用同一地址


if __name__ == '__main__':
    head = CreateListNode().create([1, 2, 3, 4, 5])
    print(Solution().FindKthToTail(head, 5))
