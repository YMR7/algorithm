package main

import (
	"fmt"
	"strings"
)


func main() {
	ans := solveNQueens(4)
	fmt.Println(ans)
}


func solveNQueens(n int) [][]string {
	board := make([][]string, n)
	for i := range board {
		var line [] string
		for j := 0; j < n; j++ {
			line = append(line, ".")
		} 
		board[i] = line
	}
	res := [][]string{}
	res = backtrack(board, 0, res)
	return res
}


func backtrack(board [][]string, row int, res [][]string) [][]string {
	size := len(board)
	if row == size {
		temp := []string{}
		for i := range board {
			line := strings.Join(board[i], "")
			temp = append(temp, line)
		}
		res =append(res, temp)
		return res
	}
	for col := 0; col < size; col++ {
		if !isValid(board, row, col) {
			continue
		}
		board[row][col] = "Q"
		res = backtrack(board, row + 1, res)
		board[row][col] = "."
	}
	return res
}


func isValid(board [][]string, row, col int) bool {
	size := len(board)
	for i := 0; i < row; i++{
		if board[i][col] == "Q" {
			return false
		}
	}
	i, j := row - 1, col + 1
	for i >= 0 && j < size {
		if board[i][j] == "Q" {
			return false
		}
		i--
		j++
	}
	i, j = row - 1, col - 1
	for i >= 0 && j >= 0 {
		if board[i][j] == "Q" {
			return false
		}
		i--
		j--
	}
	return true	
}