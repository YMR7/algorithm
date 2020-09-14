# 前　ｋ　小

import random


class Solution1:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        n = len(tinput)
        if n <= 0 or k > n:
            return []
        if k == 0:
            return []
        start = 0
        end = n - 1
        index = self.partition(tinput, start, end)
        while index != k - 1:
            if index > k - 1:
                end = index - 1
                index = self.partition(tinput, start, end)
            else:
                start = index + 1
                index = self.partition(tinput, start, end)
        res = tinput[:k]
        res = sorted(res)
        return res

    def partition(self, arr, start, end):
        if start == end:
            p = start
        else:
            p = random.randrange(start, end)
        arr[p], arr[start] = arr[start], arr[p]

        temp = arr[start]
        i = start
        j = end
        while i != j:
            # 从右往左找第一个小于temp的数
            while arr[j] >= temp and i < j:
                j -= 1
            # 从左往右找第一个大于temp的数
            while arr[i] <= temp and i < j:
                i += 1
            if i < j:
                t = arr[i]
                arr[i] = arr[j]
                arr[j] = t
        arr[start] = arr[i]
        arr[i] = temp
        return i


class Solution:
    def max_heap(self, nums, start, end):
        # 父节点
        dad = start
        # 左孩子， 不一定存在（只有一个根节点）
        son = dad * 2 + 1
        while son <= end:
            # 比较左右孩子的大小
            if son + 1 <= end and nums[son] < nums[son + 1]:
                # 右孩子
                son += 1
            # 如果父节点大于子节点表示调整完毕，直接跳出函数
            # 因为是从最后一个父节点往前调整，所有可以这样判断是否全部调整完
            if nums[dad] > nums[son]:
                return
            else:
                # 交换节点
                nums[dad], nums[son] = nums[son], nums[dad]
                dad = son
                son = dad * 2 + 1

    def GetLeastNumbers_Solution(self, tinput, k):
        lens = len(tinput)
        if k > lens or k <= 0 or lens == 0:
            return []
        res = tinput[:k]
        for i in range(k // 2 - 1, -1, -1):
            self.max_heap(res, i, k - 1)
        for i in range(k, lens):
            print(i, tinput[i], res[0])
            if tinput[i] < res[0]:
                res[0] = tinput[i]
                self.max_heap(res, 0, k-1)
        return sorted(res)


if __name__ == '__main__':
    a = list(map(int, input().split()))
    b = int(input())
    ans = Solution().GetLeastNumbers_Solution(a, b)
    print(ans)