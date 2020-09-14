"""
全排列
方法一：字典序算法
初始条件， 把字符串strs递增排序
1.从尾部找到第一个strs[i-1]<strs[i],记录i-1
2.从i（包括i）往后找最后一个大于strs[i-1]的字母，记录位置m
3.交换strs[i-1]与strs[m]
4.倒序i（包括i）之后的字母

方法二：递归算法
"""


class Solution:
    def Permutation(self, ss):
        if not ss:
            return []

        ss = list(ss)
        ss.sort(reverse=True)
        flag = ''.join(ss)
        ss.sort()
        result = [''.join(ss)]
        length = len(ss)
        while True:
            for i in range(length - 1, 0, -1):
                if ss[i - 1] < ss[i]:
                    for m in range(length - 1, i - 1, -1):
                        if ss[m] > ss[i - 1]:
                            ss[i - 1], ss[m] = ss[m], ss[i - 1]
                            ss = ss[:i] + ss[i:][::-1]
                            result.append(''.join(ss))
                            # 完成交换后，break
                            break
                    # 排列完一个字符串后break，再从头开始排列
                    break
            if flag in result:
                break

        return result



"""
递归
通过排序,来减少重复数组进入res
"""
class Solution2:
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        visited = set()
        def backtrack(nums, tmp):
            if len(nums) == len(tmp):
                res.append(tmp)
                return
            for i in range(len(nums)):
                if i in visited or (i > 0 and i - 1 not in visited and nums[i-1] == nums[i]):
                    continue
                visited.add(i)
                backtrack(nums, tmp + [nums[i]])
                visited.remove(i)
        backtrack(nums, [])
        return res


if __name__ == '__main__':
    test = Solution()
    print(test.Permutation('aabc'))
