# -*- coding: utf-8 -*-

# 定义栈的数据结构，请在该类型中实现一个能够得到栈中所含最小元素的min函数（时间复杂度应为O（1））
class Solution:
    stack = []
    assist = []

    def push(self, node):
        # write code here
        self.stack.append(node)
        if not self.assist or node <= self.assist[-1]:
            self.assist.append(node)

    def pop(self):
        pop_node = self.stack.pop()
        if pop_node == self.assist[-1]:
            self.assist.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]

    def min(self):
        if self.assist:
            return self.assist[-1]
