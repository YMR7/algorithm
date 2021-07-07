func countPrimes(n int) int {
	if n <= 2 {
		return 0
	}
	if n == 3 {
		return 1
	}
	res := 0
	for i := 4; i < n; i++ {
		if isPrime(i) {
			res++
		}
	}
	return res + 2
}

func isPrime(num int) bool {
	for j := 2; j*j <= num; j++ {
		if num%j == 0 {
			return false
		}
	}
	return true
}

// -----------方法二------------
func countPrimes2(n int) int {
	arr := make([]bool, n)
	for i := range arr {
		arr[i] = true
	}
	for i := 2; i*i < n; i++ {
		if arr[i] {
			for j := i * i; j < n; j += i {
				arr[j] = false
			}
		}
	}
	count := 0
	for i := 2; i < n; i++ {
		if arr[i] {
			count++
		}
	}
	return count
}
