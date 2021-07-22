package main

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func deleteNode(root *TreeNode, key int) *TreeNode {
	if root == nil {
		return nil
	}
	if key < root.Val {
		root.Left = deleteNode(root.Left, key)
		return root
	}
	if key > root.Val {
		root.Right = deleteNode(root.Right, key)
		return root
	}
	// 待删除节点的左右孩子皆为空
	if root.Right == nil && root.Left == nil {
		return nil
	}
	// 待删除节点的右孩子为空
	if root.Right == nil {
		return root.Left
	}
	// 待删除节点的左孩子为空
	if root.Left == nil {
		return root.Right
	}
	// 待删除节点的左右孩子皆不为空
	minNode := root.Right
	for minNode.Left != nil {
		minNode = minNode.Left
	}
	root.Val = minNode.Val
	root.Right = deleteNode(root.Right, minNode.Val)
	return root
}
