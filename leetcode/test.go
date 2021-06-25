package main

import "fmt"

func main() {
	var temp = [][3]int{}
	var aaa = [3]int{1, 2, 3}
	temp = append(temp, aaa)
	fmt.Printf("%T \n", temp)
	fmt.Printf("%T \n", temp[0])
}
