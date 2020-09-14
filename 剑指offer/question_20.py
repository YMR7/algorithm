# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））。
# 注意：保证测试中不会当栈为空的时候，对栈调用pop()或者min()或者top()方法。


class Solution:
    stack = []
    assist = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.assist  or node <= self.assist[-1]:
            self.assist.append(node)

    def pop(self):
        # write code here
        node = self.stack.pop()
        # 栈先进后出，assist pop 时不会为空
        if node == self.assist[-1]:
            self.assist.pop()

    def top(self):
        # write code here
        return self.stack[-1]

    def min(self):
        # write code here
        return self.assist[-1]