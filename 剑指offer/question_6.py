class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        # 考虑完全旋转 以及有重复数字的情况
        size = len(rotateArray)
        if size == 0:
            return 0
        elif size == 1:
            return rotateArray[0]
        else:
            # 完全旋转
            if rotateArray[-1] < rotateArray[-2]:
                return rotateArray[-1]
            else:
                left = 0
                right = size - 1
                while rotateArray[left] >= rotateArray[right]:

                    if right - left == 1:
                        # 循环退出
                        return rotateArray[right]
                    mid = left + (right - left) // 2
                    if rotateArray[left] == rotateArray[right] == rotateArray[mid]:
                        return self.has_repeat_num(left, right, rotateArray)
                    elif rotateArray[mid] >= rotateArray[left]:
                        # left != mid -1 是要考虑循环退出， 如最后只有3个数的情况
                        left = mid
                    elif rotateArray[mid] <= rotateArray[right]:
                        # 同上
                        right = mid

    def has_repeat_num(self, left, right, rotateArray):
        res = rotateArray[left]
        for num in rotateArray[left+1: right+1]:
            if num < res:
                # 根据题目意思，不会出现 5，4，3 这种情况
                return num
        # 所有数都相等
        return res