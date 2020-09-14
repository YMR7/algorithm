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
