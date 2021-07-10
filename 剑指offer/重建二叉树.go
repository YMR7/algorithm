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

func buildTree(preorder []int, inorder []int) *TreeNode {
	size := len(preorder)
	if size == 0 {
		return nil
	}else if size == 1 {
		return &TreeNode {
			Val: preorder[0],
		}
	}
	root := &TreeNode {
		Val: preorder[0],
	}
	splitIndex := 0
	for inx, val := range inorder {
		if val == preorder[0] {
			splitIndex = inx
		}
	}
	root.Left = buildTree(preorder[1:splitIndex+1], inorder[:splitIndex])
	root.Right = buildTree(preorder[splitIndex+1:], inorder[splitIndex+1:])
	return root
}