from typing import List


class Solution:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """
        递归
        """
        m = len(image)
        n = len(image[0])
        original_pixel = image[sr][sc]
        record_poi = set()
        self.helper(m, n, sr, sc, original_pixel, newColor, image, record_poi)
        return image

    def helper(self, m, n, x, y, original_pixel, new_pixel, image, record_poi):
        if (x, y) in record_poi:
            return
        record_poi.add((x, y))
        image[x][y] = new_pixel
        # left
        if y - 1 >= 0 and image[x][y - 1] == original_pixel:
            self.helper(m, n, x, y - 1, original_pixel, new_pixel, image, record_poi)
        # right
        if y + 1 < n and image[x][y + 1] == original_pixel:
            self.helper(m, n, x, y + 1, original_pixel, new_pixel, image, record_poi)
        # up
        if x - 1 >= 0 and image[x - 1][y] == original_pixel:
            self.helper(m, n, x - 1, y, original_pixel, new_pixel, image, record_poi)
        # down
        if x + 1 < m and image[x + 1][y] == original_pixel:
            self.helper(m, n, x + 1, y, original_pixel, new_pixel, image, record_poi)


class Solution2:
    def floodFill(
        self, image: List[List[int]], sr: int, sc: int, newColor: int
    ) -> List[List[int]]:
        """
        递归
        """
        m = len(image)
        n = len(image[0])
        original_pixel = image[sr][sc]
        self.helper(m, n, sr, sc, original_pixel, newColor, image)
        return image

    def helper(self, m, n, x, y, original_pixel, new_pixel, image):

        # 最后赋值，避免进入无限递归
        image[x][y] = -1
        # left
        if y - 1 >= 0 and image[x][y - 1] == original_pixel:
            self.helper(m, n, x, y - 1, original_pixel, new_pixel, image)
        # right
        if y + 1 < n and image[x][y + 1] == original_pixel:
            self.helper(m, n, x, y + 1, original_pixel, new_pixel, image)
        # up
        if x - 1 >= 0 and image[x - 1][y] == original_pixel:
            self.helper(m, n, x - 1, y, original_pixel, new_pixel, image)
        # down
        if x + 1 < m and image[x + 1][y] == original_pixel:
            self.helper(m, n, x + 1, y, original_pixel, new_pixel, image)
        image[x][y] = new_pixel


res = Solution2().floodFill([[0, 0, 0], [0, 1, 1]], 1, 1, 1)
print(res)
