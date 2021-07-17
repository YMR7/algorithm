package main

import (
	"fmt"
)

type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func pathSum(root *TreeNode, target int) [][]int {
	if root == nil {
		return nil
	}
	path := []int{}
	ans := make([][]int, 0)
	ans = recur(root, path, target, 0, ans)
	return ans
}

func recur(node *TreeNode, path []int, target int, currentSum int, res [][]int) [][]int {
	currentSum += node.Val
	path = append(path, node.Val)
	if currentSum == target && node.Left == nil && node.Right == nil {
		res = append(res, path)
		return res
	}
	track := make([]int, len(path))
	copy(track, path)
	if node.Left != nil {
		res = recur(node.Left, track, target, currentSum, res)
	}
	if node.Right != nil {
		res = recur(node.Right, track, target, currentSum, res)
	}
	return res
}

func pathSum2(root *TreeNode, sum int) [][]int {
	if root == nil {
		return nil
	}
	var ret [][]int
	dfs(root, sum, []int{}, &ret)
	return ret
}

func dfs(root *TreeNode, sum int, arr []int, ret *[][]int) {
	if root == nil {
		return
	}
	arr = append(arr, root.Val)

	if root.Val == sum && root.Left == nil && root.Right == nil {
		//slice是一个指向底层的数组的指针结构体
		//因为是先序遍历，如果 root.Right != nil ,arr 切片底层的数组会被修改
		//所以这里需要 copy arr 到 tmp，再添加进 ret，防止 arr 底层数据修改带来的错误
		// tmp := make([]int,len(arr))
		// copy(tmp,arr)
		// *ret = append(*ret,tmp)
		*ret = append(*ret, append([]int{}, arr...))
	}

	dfs(root.Left, sum-root.Val, arr, ret)
	dfs(root.Right, sum-root.Val, arr, ret)
}

func main() {
	a := &TreeNode{Val: -2}
	b := &TreeNode{Val: -3}
	a.Right = b
	ans := pathSum2(a, -5)
	fmt.Println(ans)
}
