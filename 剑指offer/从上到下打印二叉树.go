/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func levelOrder(root *TreeNode) []int {
	if root == nil {
		return nil
	}
	li := make([]*TreeNode, 0)
	res := make([]int, 0)
	li = append(li, root)
	for len(li) > 0 {
		node := li[0]
		res = append(res, node.Val)
		if node.Left != nil {
			li = append(li, node.Left)
		}
		if node.Right != nil {
			li = append(li, node.Right)
		}
		li = li[1:]
	}
	return res
}