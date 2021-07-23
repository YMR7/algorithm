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


// ---------------------way 2-------------------------
func isValidBST(root *TreeNode) bool {
	return recur(root, nil, nil)
}

func recur(root *TreeNode, minNode *TreeNode, maxNode *TreeNode) bool {
	if root == nil {
		return true
	}
	if minNode != nil && root.Val <= minNode.Val {
		return false
	}
	if maxNode != nil && root.Val >= maxNode.Val {
		return false
	}
	return recur(root.Left, minNode, root) && recur(root.Right, root, maxNode)
}