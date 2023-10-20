package main

import (
	"bufio"
	"fmt"
	"image"
	"log"
	"os"
)

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	scanner := bufio.NewScanner(file)
	trees := map[image.Point]rune{}
	y := 0
	for scanner.Scan() {
		row := scanner.Text()
		for x, height := range row {
			trees[image.Point{x, y}] = height
		}
		y++
	}

	visible := 0
	highestScenicScore := 0
	deltas := []image.Point{{0, -1}, {0, 1}, {-1, 0}, {1, 0}}
	for coords, treeHeight := range trees {
		treeVisible := false
		scenicScore := 1
		for _, delta := range deltas {
			for i := 1; ; i++ {
				newCoords := coords.Add(delta.Mul(i))
				newTreeHeight, ok := trees[newCoords]
				if !ok {
					treeVisible = true
					scenicScore *= i - 1
					break
				}
				if newTreeHeight >= treeHeight {
					scenicScore *= i
					break
				}
			}
		}

		if treeVisible {
			visible++
		}

		if scenicScore > highestScenicScore {
			highestScenicScore = scenicScore
		}
	}

	fmt.Println("Answer One", visible)

	fmt.Println("Answer Two", highestScenicScore)
}
