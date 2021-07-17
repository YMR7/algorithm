type TreeNode struct {
	Val   int
	Left  *TreeNode
	Right *TreeNode
}

func kthLargest(root *TreeNode, k int) int {
	order := dfs(root, []int{})
	size := len(order)
	return order[size-k]

}

func dfs(root *TreeNode, sortNode []int) []int {
	if root == nil {
		return sortNode
	}
	sortNode = dfs(root.Left, sortNode)
	sortNode = append(sortNode, root.Val)
	sortNode = dfs(root.Right, sortNode)
	return sortNode
}

// -------------way 2-------------

func kthLargest(root *TreeNode, k int) int {
	order := make([]int, 0)
	dfs(root, &order)
	return order[k-1]

}

func dfs(root *TreeNode, order *[]int) {
	if root != nil {
		dfs(root.Right, order)
		*order = append(*order, root.Val)
		dfs(root.Left, order)
	}
}


// -------------way 3----------------------
var skip int
var res int
func kthLargest(root *TreeNode, k int) int {
    skip = k
    res = 0
    dfs(root)
    return res
}

func dfs(root *TreeNode){
    if root != nil{
        dfs(root.Right)
        skip--
        if skip == 0{
            res = root.Val
            return
        }
        dfs(root.Left)
    }
}


// --------way 4-----------
func kthLargest(root *TreeNode, k int) (res int) {
	var recur func(root *TreeNode)
	recur = func(root *TreeNode) {
		if root == nil || k == 0 {
			return
		}
		recur(root.Right)
		k--
		if k == 0 {
			res = root.Val
			return
		}
		recur(root.Left)
	}
	recur(root)
	return
}