func minDistance(word1 string, word2 string) int {
	size1 := len(word1)
	size2 := len(word2)
	dp := make([][]int, size1+1)
	for i := range dp {
		dp[i] = make([]int, size2+1)
	}
	for i := 0; i <= size1; i++ {
		dp[i][0] = i
	}
	for j := 0; j <= size2; j++ {
		dp[0][j] = j
	}
	for i := 1; i <= size1; i++ {
		for j := 1; j <= size2; j++ {
			if word1[i-1] == word2[j-1] {
				dp[i][j] = dp[i-1][j-1]
			} else {
				del_c := dp[i-1][j]
				replace_c := dp[i-1][j-1]
				add_c := dp[i][j-1]
				dp[i][j] = min(del_c, replace_c, add_c) + 1
			}
		}
	}
	return dp[size1][size2]
}

func min(a ...int) int {
	res := a[0]
	for _, val := range a[1:] {
		if val < res {
			res = val
		}
	}
	return res
}