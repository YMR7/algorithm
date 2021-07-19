package main

import "fmt"

func isMatch(s string, p string) bool {
	return recur(s, p, 0, 0)
}

func recur(s string, p string, i int, j int) bool {
	res := true
	sizeS := len(s)
	sizeP := len(p)
	if i == sizeS {
		if (sizeP-j)%2 == 1 {
			return false
		} else {
			for ; j+1 < sizeP; j += 2 {
				if p[j+1] != '*' {
					return false
				}
			}
			return true
		}
	}
	if j == sizeP {
		return i == sizeS
	}

	if j+1 < sizeP && p[j+1] == '*' {
		if s[i] != p[j] && p[j] != '.' {
			res = recur(s, p, i, j+2)
		} else {
			res = recur(s, p, i+1, j) || recur(s, p, i, j+2)
		}
	} else {
		if s[i] == p[j] || p[j] == '.' {
			res = recur(s, p, i+1, j+1)
		} else {
			res = false
		}
	}
	return res
}

func main() {
	ans := isMatch("aab", "c*a*b")
	fmt.Println(ans)
}
