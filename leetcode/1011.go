
func shipWithinDays(weights []int, days int) int {
	left := max(weights...)
	right := sum(weights...) + 1
	for left < right {
		mid := left + (right-left)/2
		if isEnough(days, mid, weights) {
			right = mid
		} else {
			left = mid + 1
		}
	}
	return left
}

func isEnough(days int, limit int, weights []int) bool {
	count := 0
	for i := 0; i < days; i++ {
		for temp := limit - weights[count]; temp >= 0; temp -= weights[count] {
			count++
			if count == len(weights) {
				return true
			}
		}
	}
	return false
}

func max(a ...int) int {
	res := a[0]
	for _, val := range a[1:] {
		if val > res {
			res = val
		}
	}
	return res
}

func sum(a ...int) int {
	res := a[0]
	for _, val := range a[1:] {
		res += val
	}
	return res
}
