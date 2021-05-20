from typing import List


class Solution:
    def __init__(self) -> None:
        self.res = []

    def combine(self, n: int, k: int) -> List[List[int]]:
        track = []
        self.backtrack(track, n, k, 1)
        return self.res

    def backtrack(self, track, n, k, start):
        if len(track) == k:
            temp = track.copy()
            self.res.append(temp)
            return
        for num in range(start, n + 1):
            track.append(num)
            # 关键在 start 为 num + 1
            self.backtrack(track, n, k, num + 1)
            track.pop()


if __name__ == '__main__':
    res = Solution().combine(4, 2)
    print(res)