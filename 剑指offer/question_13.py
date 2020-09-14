class Solution:
    def reOrderArray(self, array):
        # write code here
        # 插入排序
        if not array:
            return []
        size = len(array)
        # 记录已排序的奇数的个数
        count = 0
        for i in range(size):
            if array[i] % 2 == 1:
                temp = array[i]
                while i > count:
                    array[i] = array[i - 1]
                    i -= 1
                array[count] = temp
                count += 1
        return array


if __name__ == '__main__':
    print(Solution().reOrderArray([1, 2, 3, 4, 5, 6, 7]))
