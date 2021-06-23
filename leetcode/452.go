package main

import "sort"


func findMinArrowShots(points [][]int) int {
	size := len(points)
	if size == 0 {
		return 0
	}
	sort.Slice(points, func(i, j int) bool { return points[i][0] < points[j][0]})
	dp := make([]int, size)
	for i := range dp {
		dp[i] = 1
	}
	for i := 1; i < size; i++ {
		for j := 0; j < i; j++{
			if points[i][0] > points[j][1] {
				dp[i] = max(dp[i], dp[j] + 1)
			}
		}
	}
	return max(dp...)
}


func max(a ...int) int {
	res := a[0]
	for _, v := range a[1:] {
		if v > res {
			res = v
		}
	}
	return res
}