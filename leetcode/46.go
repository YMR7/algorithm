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
    backtrack(nums, record, res)
    return res
}

func backtrack(nums, track []int, ans [][]int) {
    size := len(nums)
    if size == len(track) {
        fmt.Println(ans)
        temp := make([]int, size)
        copy(temp, track)
        ans = append(ans, temp)
        fmt.Println(ans)
        return
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
        backtrack(nums, track, ans)
        track = track[:len(track) - 1]
    }
}