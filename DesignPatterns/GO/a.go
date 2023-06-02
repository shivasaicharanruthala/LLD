package main

import "fmt"

func main() {
	s := []int{2, 3, 4, 6, 7}
	printSlice(s)

	//s = s[3:]

	s = append(s, []int{1, 2, 6, 8, 9, 78}...)
	printSlice(s)
}

func printSlice(s []int) {
	fmt.Printf("len=%d cap=%d %v\n", len(s), cap(s), s)
}
