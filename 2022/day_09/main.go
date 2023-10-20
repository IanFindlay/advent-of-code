package main

import (
	"bufio"
	"fmt"
	"image"
	"os"
	"strconv"
	"strings"
)

type Move struct {
	direction string
	distance  int
}

func moveTail(head *image.Point, tail *image.Point, movements map[string]image.Point) {
	xDist := head.X - tail.X
	yDist := head.Y - tail.Y

	if xDist > 1 || xDist < -1 || yDist > 1 || yDist < -1 {
		var xMove image.Point
		if xDist < 0 {
			xMove = movements["left"]
		} else if xDist > 0 {
			xMove = movements["right"]
		}
		*tail = tail.Add(xMove)

		var yMove image.Point
		if yDist < 0 {
			yMove = movements["down"]
		} else if yDist > 0 {
			yMove = movements["up"]
		}
		*tail = tail.Add(yMove)
	}
}

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	moves := []Move{}
	for scanner.Scan() {
		line := strings.Split(scanner.Text(), " ")
		distance, _ := strconv.Atoi(line[1])
		moves = append(moves, Move{direction: line[0], distance: distance})
	}

	movements := map[string]image.Point{
		"up": {0, 1}, "down": {0, -1}, "left": {-1, 0}, "right": {1, 0},
	}

	start := image.Point{0, 0}
	knots := [10]image.Point{
		start, start, start, start, start,
		start, start, start, start, start,
	}
	visitedSetOne := map[image.Point]bool{knots[1]: true}
	visitedSetTwo := map[image.Point]bool{knots[9]: true}
	for _, move := range moves {
		for i := 0; i < move.distance; i++ {
			switch move.direction {
			case "U":
				knots[0] = knots[0].Add(movements["up"])
			case "D":
				knots[0] = knots[0].Add(movements["down"])
			case "L":
				knots[0] = knots[0].Add(movements["left"])
			case "R":
				knots[0] = knots[0].Add(movements["right"])
			}

			for i := 1; i < 10; i++ {
				moveTail(&knots[i-1], &knots[i], movements)
			}
			visitedSetOne[knots[1]] = true
			visitedSetTwo[knots[9]] = true
		}
	}

	fmt.Println("Answer One:", len(visitedSetOne))

	fmt.Println("Answer Two:", len(visitedSetTwo))
}
