from typing import List


class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: x[1])
        count = 1
        end = points[0][1]
        for interval in points:
            start = interval[0]
            if start > end:
                count += 1
                end = interval[1]
        return count
