package main

import (
	"fmt"
	"math"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isBalanced(root *TreeNode) bool {
	if root == nil {
		return true
	}

	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	if math.Abs(float64(leftDepth-rightDepth)) > 1 {
		return false
	}
	return isBalanced(root.Left) && isBalanced(root.Right)

}

func maxDepth(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftDepth := maxDepth(root.Left)
	rightDepth := maxDepth(root.Right)
	return max(leftDepth, rightDepth) + 1
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

// ---------way 2--------
func isBalanced2(root *TreeNode) bool {
	return recur(root) != -1
}

func recur(root *TreeNode) int {
	if root == nil {
		return 0
	}
	leftDepth := recur(root.Left)
	if leftDepth == -1 {
		return -1
	}
	rightDepth := recur(root.Right)
	if rightDepth == -1 {
		return -1
	}
	if math.Abs(float64(leftDepth-rightDepth)) > 1 {
		return -1
	}
	return max(leftDepth, rightDepth) + 1
}

func main() {
	a := &TreeNode{Val: 1}
	b := &TreeNode{Val: 2}
	c := &TreeNode{Val: 3}
	a.Left = b
	b.Left = c
	ans := isBalanced(a)
	fmt.Println(ans)
}
