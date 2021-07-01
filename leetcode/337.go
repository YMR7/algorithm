/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */

type TreeNode struct {
	Val int
	Left *TreeNode
	Right *TreeNode
}

func rob(root *TreeNode) int {
	record := map[*TreeNode]int{}
	ans := dp(root, record)
	return ans
}

func dp(root *TreeNode, memo map[*TreeNode]int) int {
	if root == nil {
		return 0
	}
	if value, ok := memo[root]; ok {
		return value
	}
	rob_it:= root.Val
	if root.Left != nil {
		rob_it += dp(root.Left.Left, memo) + dp(root.Left.Right, memo)
	}
	if root.Right != nil {
		rob_it += dp(root.Right.Left, memo) + dp(root.Right.Right, memo)
	}
	not_rob_it := dp(root.Left, memo) + dp(root.Right, memo)
	res := max(rob_it, not_rob_it)
	memo[root] = res
	return res
}

func rob2(root *TreeNode) int {
	ans := dp2(root)
	return max(ans[0], ans[1])
}

func dp2(root *TreeNode) []int {
	// res[0] 表示不抢 root 可获得的最大数
	// res[1] 表示抢 root 可获得的最大数
	if root == nil {
		res := []int{0, 0}
		return res
	}
	left := dp2(root.Left)
	right := dp2(root.Right)
	rob_it := root.Val + left[0] + right[0]
	not_rob_it := max(left[0], left[1]) + max(right[0], right[1])
	res := []int{not_rob_it, rob_it}
	return res
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}