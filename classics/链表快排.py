class Solution():
    """快排类"""
    def __init__(self):
        pass

    # end 初始为 None
    def quicksorted(self, head, end):
        if head != end:
            node = self.partition(head, end)          # 先挖坑填数
            self.quicksorted(head, node)              # 递归调用
            self.quicksorted(node.next, end)          # 递归调用

    def partition(self, head, end):
        p1, p2 = head, head.next        # p2是遍历指针，p1是小数的指针

        while p2 != end:
            if p2.value < head.value:
                p1 = p1.next

                tmp = p2.value
                p2.value = p1.value
                p1.value = tmp
            p2 = p2.next

        tmp = head.value
        head.value = p1.value
        p1.value = tmp

        return p1
