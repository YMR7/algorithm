func trap(height []int) int {
	if len(height) <= 1 {
		return 0
	}
	maxHeight := 0
	maxHeightIndex := 0
	for inx, val := range height {
		if val > maxHeight {
			maxHeight = val
			maxHeightIndex = inx
		}
	}
	res := 0
	temp := height[0]
	for i := 0; i <= maxHeightIndex; i++ {
		if temp > height[i] {
			res += temp - height[i]
		} else {
			temp = height[i]
		}
	}
	right := len(height) - 1
	temp2 := height[right]
	for ; right >= maxHeightIndex; right-- {
		if temp2 > height[right] {
			res += temp2 - height[right]
		} else {
			temp2 = height[right]
		}
	}
	return res
}


