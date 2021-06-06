from typing import List


class Solution:
    def intervalIntersection(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        size_first = len(firstList)
        size_second = len(secondList)
        i, j = 0, 0
        res = []
        while i < size_first and j < size_second:
            left_max = max(firstList[i][0], secondList[j][0])
            right_min = min(firstList[i][1], secondList[j][1])
            # 无交集
            if left_max > right_min:
                if left_max == firstList[i][0]:
                    # list-1 在右
                    j += 1
                else:
                    # list-1 在左
                    i += 1
            else:
                if left_max == firstList[i][0] and right_min == secondList[j][1]:
                    # list-1 右，list-2 左，部分相交
                    j += 1
                    res.append([left_max, right_min])
                elif left_max == secondList[j][0] and right_min == firstList[i][1]:
                    # list-1 左，list-2 右，部分相交
                    i += 1
                    res.append([left_max, right_min])
                elif left_max == secondList[j][0] and right_min == secondList[j][1]:
                    # list-1 包含 list-2
                    j += 1
                    res.append([left_max, right_min])
                elif left_max == firstList[i][0] and right_min == firstList[i][1]:
                    # list-2 包含 list-1
                    i += 1
                    res.append([left_max, right_min])
        return res

    def intervalIntersection2(
        self, firstList: List[List[int]], secondList: List[List[int]]
    ) -> List[List[int]]:
        size_first = len(firstList)
        size_second = len(secondList)
        i, j = 0, 0
        res = []
        while i < size_first and j < size_second:
            a1, a2 = firstList[i]
            b1, b2 = secondList[j]
            if b2 >= a1 and a2 >= b1:
                res.append([max(a1, b1), min(a2, b2)])
            if a2 > b2:
                j += 1
            else:
                i += 1
        return res


ans = Solution().intervalIntersection2(
    [[3, 5], [9, 20]], [[4, 5], [7, 10], [11, 12], [14, 15], [16, 20]]
)
print(ans)
