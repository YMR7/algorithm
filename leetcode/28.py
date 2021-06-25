class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        size_1 = len(haystack)
        size_2 = len(needle)
        if not size_2:
            return 0
        if size_1 < size_2:
            return -1
        for i in range(size_1 - size_2 + 1):
            if haystack[i : i + size_2] == needle:
                return i
        return -1
