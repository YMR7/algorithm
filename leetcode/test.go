package main
 
import (
    "fmt"
)
 
func main() {
    var baseArr = []int{1,2,3}
    var part1 = baseArr[2:]              // [1] cap 3
    // var part2 = baseArr[1:]              // [2,3] cap 2
    var result [][]int
    for  i := 0; i < 10; i++ {
        fmt.Println(cap(part1))
        part1 := append(part1, i) // （2）
        fmt.Println(cap(part1))
        fmt.Println(part1)
        // fmt.Println(tempArr)
        fmt.Println(baseArr)
        fmt.Println("===============")
        // result = append(result, tempArr)   // （3）
    }
    fmt.Println(result)
}

// 牛啤堂
// 北平机器

