package main

import (
	"fmt"
	"strconv"
	// "strings"
)

func main() {
	ans := isMatch("aa", "w*a*")
	fmt.Println(ans)
}

func isMatch(s string, p string) bool {
	// arrS := strings.Split(s, "")
	// arrP := strings.Split(p, "")
	memo := map[string]bool{}
	return dp(s, p, 0, 0, memo)
}

func dp(s string, p string, i int, j int, memo map[string]bool) bool {
	sizeS := len(s)
	sizeP := len(p)
	res := false
	if j == sizeP {
		return i == sizeS
	}
	if i == sizeS {
		if (sizeP-j)%2 == 1 {
			return false
		}
		for ; j+1 < sizeP; j += 2 {
			if p[j+1] != '*' {
				return false
			}
		}
		return true
	}
	theKey := strconv.Itoa(i) + "-" + strconv.Itoa(j)
	if value, ok := memo[theKey]; ok {
		return value
	}
	if s[i] == p[j] || p[j] == '.' {
		if j+1 < sizeP && p[j+1] == '*' {
			res = dp(s, p, i, j+2, memo) || dp(s, p, i+1, j, memo)
		} else {
			res = dp(s, p, i+1, j+1, memo)
		}
	} else {
		if j+1 < sizeP && p[j+1] == '*' {
			res = dp(s, p, i, j+2, memo)
		} else {
			res = false
		}
	}
	memo[theKey] = res
	return memo[theKey]
}
