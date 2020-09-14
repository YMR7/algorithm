# 两个栈实现一个队列

class Solution:
    node_in = []
    node_out = []

    def push(self, node):
        # write code here
        self.node_in.append(node)

    def pop(self):
        # return xx
        if not self.node_out:
            while self.node_in:
                self.node_out.append(self.node_in.pop())
        return self.node_out.pop()


# 两个队列实现一个栈
class MyStack(object):

    def __init__(self):
        # 初始化
        self.mainQueue = []
        self.assistQueue = []

    def push(self, x):
        #将新元素放在辅助队列的队首
        self.assistQueue.append(x)
        #让mainQueue中的所有元素通过pop的方式被吐出来，然后放入assistQueue的队尾
        if len(self.mainQueue) != 0:
            self.assistQueue.extend(self.mainQueue)
        #现在assistQueue是完整的队列了，现在交换两个队列的名字，方便之后使用
        self.mainQueue = self.assistQueue
        self.assistQueue = []

    def pop(self):
        #吐出第一个元素
        return self.mainQueue.pop(0)

    def top(self):
        #读取第一个元素
        return self.mainQueue[0]

    def empty(self):
        #使用len()判断队列是否为空
        return len(self.mainQueue) == 0

# 用 deque
from collections import deque
class MyStack:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.data = deque()
        self.help = deque()
    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        self.data.append(x)
    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        while len(self.data) > 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help,self.data = self.data,self.help
        return tmp
    def top(self) -> int:
        """
        Get the top element.
        """
        while len(self.data) != 1:
            self.help.append(self.data.popleft())
        tmp = self.data.popleft()
        self.help.append(tmp)
        self.help,self.data = self.data,self.help
        return tmp
    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not bool(self.data)
