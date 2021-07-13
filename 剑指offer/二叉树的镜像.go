type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func mirrorTree(root *TreeNode) *TreeNode {
	if root == nil {
		return root
	}
	l := mirrorTree(root.Left)
	r := mirrorTree(root.Right)
	root.Left = r
	root.Right = l
	return root
}