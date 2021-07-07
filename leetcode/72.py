class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        return self.helper(len(word1) - 1, len(word2) - 1, word1, word2)

    def helper(self, i, j, word1, word2):
        if i == -1:
            return j + 1
        if j == -1:
            return i + 1
        if word1[i] == word2[j]:
            return self.helper(i - 1, j - 1, word1, word2)
        else:
            del_c = self.helper(i - 1, j, word1, word2)
            replace_c = self.helper(i - 1, j - 1, word1, word2)
            add_c = self.helper(i, j - 1, word1, word2)
            return min(del_c, replace_c, add_c) + 1


class Solution2:
    def minDistance(self, word1: str, word2: str) -> int:
        memo = {}
        return self.helper(len(word1) - 1, len(word2) - 1, word1, word2, memo)

    def helper(self, i, j, word1, word2, memo):
        if (i, j) in memo:
            return memo[(i, j)]
        if i == -1:
            return j + 1
        if j == -1: 
            return i + 1
        if word1[i] == word2[j]:
            memo[(i, j)] = self.helper(i - 1, j - 1, word1, word2, memo)
        else:
            del_c = self.helper(i - 1, j, word1, word2, memo)
            replace_c = self.helper(i - 1, j - 1, word1, word2, memo)
            add_c = self.helper(i, j - 1, word1, word2, memo)
            memo[(i, j)] = min(del_c, replace_c, add_c) + 1
        return memo[(i, j)]


class Solution3:
    def minDistance(self, word1: str, word2: str) -> int:
        size_1 = len(word1)
        size_2 = len(word2)
        dp = [[0] * (size_2 + 1) for _ in range(size_1 + 1)]
        for j in range(size_2 + 1):
            dp[0][j] = j
        for i in range(size_1 + 1):
            dp[i][0] = i
        for i in range(1, size_1 + 1):
            for j in range(1, size_2 + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    del_c = dp[i - 1][j]
                    replace_c = dp[i - 1][j - 1]
                    add_c = dp[i][j - 1]
                    dp[i][j] = min(del_c, replace_c, add_c) + 1
        return dp[size_1][size_2]


ans = Solution3().minDistance("horse", "ros")
print(ans)