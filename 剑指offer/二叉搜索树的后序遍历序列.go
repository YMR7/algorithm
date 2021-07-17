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

func verifyPostorder(postorder []int) bool {
	return recur(postorder, 0, len(postorder)-1)
}

func recur(postorder []int, left int, right int) bool {
	if left >= right {
		return true
	}
	splitIndex := left
	root := postorder[right]
	for postorder[splitIndex] < root {
		splitIndex++
	}
	checkRightTree := splitIndex
	for postorder[checkRightTree] > root {
		checkRightTree++
	}
	return checkRightTree == right && recur(postorder, left, splitIndex-1) && recur(postorder, splitIndex, right-1)
}

func verifyPostorder2(postorder []int) bool {
	root := math.MaxInt64
	stack := make([]int, 0)
	for i := len(postorder)-1; i >= 0; i-- {
		if postorder[i] > root {
			return false
		}
		for len(stack) > 0 && postorder[i] < stack[len(stack)-1] {
			root = stack[len(stack)-1]
			stack = stack[:len(stack)-1]
		}
		stack = append(stack, postorder[i])
	}
	return true
}

func main() {
	postorder := []int{1, 6, 3, 2, 5}
	ans := verifyPostorder2(postorder)
	fmt.Println(ans)
}
