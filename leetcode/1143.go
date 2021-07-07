func longestCommonSubsequence(text1 string, text2 string) int {
	size1 := len(text1)
	size2 := len(text2)
	dp := make([][]int, size1+1)
	for inx := range dp {
		dp[inx] = make([]int, size2+1)
	}
	for i := 1; i < size1+1; i++ {
		for j := 1; j < size2+1; j++ {
			flag := 0
			if text1[i-1] == text2[j-1] && flag == 0{
				flag = 1
				dp[i][j] = dp[i-1][j-1]+ 1
			} else {
				dp[i][j] = max(dp[i-1][j], dp[i][j-1])
			}
		}
	}
	return dp[size1][size2]
}

func max(a ...int) int {
	res := a[0]
	for _, num := range a[1:] {
		if num > res {
			res = num
		}
	}
	return res
}
