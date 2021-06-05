from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        size = len(intervals)
        res = []
        cur_min = intervals[0][0]
        cur_max = intervals[0][1]
        for i in range(1, size):
            if intervals[i][0] <= cur_max:
                # 前一个区间完全覆盖后一个区间
                cur_max = max(cur_max, intervals[i][1])
            else:
                res.append([cur_min, cur_max])
                cur_min = intervals[i][0]
                cur_max = intervals[i][1]
        res.append([cur_min, cur_max])
        return res


ans = Solution().merge([[1, 3], [2, 6], [8, 10], [15, 18]])
print(ans)
