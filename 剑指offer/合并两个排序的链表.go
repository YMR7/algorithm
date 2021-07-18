/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */

type ListNode struct {
	Val int
	Next *ListNode
}

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}
	maxList := l2
	minList := l1
	if l1.Val > l2.Val {
		maxList = l1
		minList = l2
	}
	head := &ListNode{
		Val: minList.Val,
	}
	curNode := head 
	minList = minList.Next
	for minList != nil && maxList != nil {
		if minList.Val < maxList.Val {
			temp := &ListNode{
				Val: minList.Val,
			}
			curNode.Next = temp
			curNode = curNode.Next
			minList = minList.Next
		} else {
			temp := &ListNode{
				Val: maxList.Val,
			}
			curNode.Next = temp
			curNode = curNode.Next
			maxList = maxList.Next
		}
	}
	if minList != nil {
		curNode.Next = minList
	} else if maxList != nil {
		curNode.Next = maxList
	}
	return head
}


// --------way 2----------------

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}
	maxList := l2
	minList := l1
	if l1.Val > l2.Val {
		maxList = l1
		minList = l2
	}
	head := &ListNode{
		Val: minList.Val,
	}
	curNode := head 
	minList = minList.Next
	for minList != nil && maxList != nil {
		if minList.Val < maxList.Val {
			curNode.Next = minList
			minList = minList.Next
		} else {
			curNode.Next = maxList
			maxList = maxList.Next
		}
		curNode = curNode.Next

	}
	if minList != nil {
		curNode.Next = minList
	} else if maxList != nil {
		curNode.Next = maxList
	}
	return head
}

// --------way 3----------------

func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil {
		return l2
	} else if l2 == nil {
		return l1
	}
	if l1.Val < l2.Val {
		l1.Next = mergeTwoLists(l1.Next, l2)
		return l1
	} else {
		l2.Next = mergeTwoLists(l2.Next, l1)
		return l2
	}
}
