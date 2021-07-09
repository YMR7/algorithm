func minEatingSpeed(piles []int, h int) int {
	left := 1
	right := max(piles) + 1
	for left < right {
		mid := left + (right - left) / 2
		if isEnough(mid, piles, h) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func isEnough(speed int, piles []int, h int) bool {
	count := 0
	for _, val := range piles {
		count += needTime(speed, val)
	}
	return count <= h
}

func needTime(speed, num int) int {
	res := num / speed
	if num % speed != 0 {
		res++
	}
	return res

}

func max(a ...int) int {
	res := a[0]
	for _, val := range res[1:] {
		if val > res {
			res = val
		}
	}
	return res
}