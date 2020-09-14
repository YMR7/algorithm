# 二分查找解法
class Solution:
    # array 二维列表
    def binary_search(self, target, nums):
        if not nums:
            return False
        size = len(nums)
        mid = size // 2

        if target > nums[mid]:
            return self.binary_search(target, nums[mid + 1:])
        elif target < nums[mid]:
            return self.binary_search(target, nums[:mid])
        else:
            return True

    def find(self, target, array):
        # write code here
        # {[]} ！= None
        if not array[0]:
            return
        row = len(array) - 1
        # 排除不可能行
        while target < array[row][0]:
            row -= 1
            if row < 0:
                return False
        while row >= 0:
            nums = array[row]
            flag = self.binary_search(target, nums)
            if flag:
                return True
            row -= 1
        return False


# 解法二
class Solution2:
    def find(self, target, array):
        if not array[0]:
            return
        row = len(array)
        col = len(array[0])
        i = row - 1
        j = 0
        temp = array[i][j]
        while temp != target:
            if temp < target:
                j += 1
            else:
                i -= 1
            if j < col and i >= 0:
                temp = array[i][j]
            else:
                return False
        return temp == target


if __name__ == '__main__':
    array = [[1, 2, 8, 9], [2, 4, 9, 12], [4, 7, 10, 13], [6, 8, 11, 15]]
    target = 0
    print(Solution2().find(target, array))
