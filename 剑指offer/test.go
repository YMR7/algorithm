package main

import "fmt"

func main() {
	a := &TreeNode{
		Val:3,
	}
	b := &TreeNode{
		Val:2,
	}
	c := &TreeNode{
		Val:1,
	}
	a.Left = b
	a.Right = c
	bak := a
	ans := mirrorTree(a)
	fmt.Println(ans)
	fmt.Println(bak)
}

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
