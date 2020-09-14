# -*- coding: utf-8 -*-
"""
题目描述
每年六一儿童节,牛客都会准备一些小礼物去看望孤儿院的小朋友,
今年亦是如此。HF作为牛客的资深元老,自然也准备了一些小游戏。
其中,有个游戏是这样的:首先,让小朋友们围成一个大圈。然后,他
随机指定一个数m,让编号为0的小朋友开始报数。每次喊到m-1的那
个小朋友要出列唱首歌,然后可以在礼品箱中任意的挑选礼物,并且不
再回到圈中,从他的下一个小朋友开始,继续0...m-1报数....
这样下去....直到剩下最后一个小朋友,可以不用表演,并且拿到
牛客名贵的“名侦探柯南”典藏版(名额有限哦!!^_^)。请你试着想下,
哪个小朋友会得到这份礼品呢？(注：小朋友的编号是从0到n-1)

如果没有小朋友，请返回-1
"""


class Solution:
    def test(self, n, m):
        loop = list(range(n))
        people = 0
        while len(loop) > 1:
            people = (people + m - 1) % len(loop)
            loop.pop(people)
        return loop[0]+1 if len(loop) == 1 else -1


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class Solution2:
    def lastRemaining(self, n: int, m: int) -> int:
        if not n:
            return
        root = Node(0)
        pos = root
        for num in range(1, n):
            node = Node(num)
            pos.next = node
            pos = pos.next
        pos.next = root
        while pos != pos.next:
            for i in range(m):
                if i == m - 1:
                    pos.next = pos.next.next
                else:
                    pos = pos.next
        return pos.val


class Solution3:
    def lastRemaining(self, n: int, m: int) -> int:
        res = 0
        for i in range(2,n+1):
            res = (res+m)%i
        return res


if __name__ == '__main__':
    N, M = map(int, input().split())
    print(Solution().test(N, M))