package main

import "fmt"

func main() {
    nums := []int{1,2,3}
    ans := permute(nums)
    fmt.Println(ans)
}


func permute(nums []int) [][]int {
    // var res = [][]int{}
    res := [][]int{}
    record := []int{}
    ans := backtrack(nums, record, res)
    return ans
}

func backtrack(nums, track []int, ans [][]int) [][]int {
    size := len(nums)
    if size == len(track) {
        temp := make([]int, size)
        copy(temp, track)
        ans = append(ans, temp)
        return ans
    }
    for _, num := range nums {
        flag := 0
        for _, temp := range track {
            if temp == num {
                flag = 1
                break
            }
        }
        if flag == 1 {
            continue
        }
        track = append(track, num)
        ans = backtrack(nums, track, ans)
        track = track[:len(track) - 1]
    }
    return ans
}