package main

import "fmt"

func main() {
	preorder := []int{3,9,20,15,7}
	inorder := []int{9,3,15,20,7}
	ans := buildTree(preorder, inorder)
	fmt.Println(ans)
}

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
	if root.Left == nil {
		fmt.Println("================")
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