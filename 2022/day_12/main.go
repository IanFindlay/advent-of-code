package main

import (
	"fmt"
	"image"
	"os"
	"strings"
)

func bfs(start image.Point, endValue rune, heightMap map[image.Point]rune, partOne bool) int {
	deltas := []image.Point{{1, 0}, {-1, 0}, {0, 1}, {0, -1}}

	queue := []image.Point{start}
	steps := map[image.Point]int{start: 0}
	for len(queue) > 0 {
		current := queue[0]
		queue = queue[1:]
		currentHeight := heightMap[current]

		for _, delta := range deltas {
			neighbour := current.Add(delta)

			_, visited := steps[neighbour]
			if visited {
				continue
			}

			neighbourHeight, valid := heightMap[neighbour]
			if !valid {
				continue
			}

			if partOne {
				if neighbourHeight <= currentHeight+1 {
					queue = append(queue, neighbour)
					steps[neighbour] = steps[current] + 1
				} else {
					continue
				}
			} else {
				if neighbourHeight >= currentHeight-1 {
					queue = append(queue, neighbour)
					steps[neighbour] = steps[current] + 1
				} else {
					continue
				}
			}

			if neighbourHeight == endValue {
				return steps[current] + 1
			}
		}
	}

	return -1
}

func main() {
	file, _ := os.ReadFile("input.txt")
	rows := strings.Split(string(file), "\n")
	heightMap := map[image.Point]rune{}
	var endCoords image.Point
	var startCoords image.Point
	for y, row := range rows {
		for x, rune := range row {
			point := image.Point{x, y}
			heightMap[point] = rune
			if rune == 'E' {
				endCoords = point
			}
			if rune == 'S' {
				startCoords = point
				heightMap[point] = 'a'
			}
		}
	}

	fewestSteps := bfs(startCoords, heightMap[endCoords], heightMap, true)
	fmt.Println("Answer One:", fewestSteps)

	heightMap[endCoords] = 'z'
	fewestSteps = bfs(endCoords, heightMap[startCoords], heightMap, false)
	fmt.Println("Answer Two:", fewestSteps)
}
