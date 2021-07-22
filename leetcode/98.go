type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func isValidBST(root *TreeNode) bool {
	if root == nil {
		return true
	}
	order := make([]int, 0)
	inorder(root, &order)
	tmp := order[0]
	for _, num := range order[1:] {
		if tmp >= num {
			return false
		}
		tmp = num
	}
	return true
}

func inorder(root *TreeNode, order *[]int) {
	if root == nil {
		return
	}
	inorder(root.Left, order)
	*order = append(*order, root.Val)
	inorder(root.Right, order)
}