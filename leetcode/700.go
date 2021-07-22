type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func searchBST(root *TreeNode, val int) *TreeNode {
	if root == nil {
		return nil
	}
	res := &TreeNode{}
	if root.Val == val {
		res = root
	} else if root.Val > val {
		res = searchBST(root.Left, val)
	} else {
		res = searchBST(root.Right, val)
	}
	return res
}