package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Coord struct {
	x int
	y int
}

func main() {
	file, _ := os.ReadFile("input.txt")
	rows := strings.Split(strings.TrimSpace(string(file)), "\n")
	rocks := map[Coord]bool{}
	settledSand := map[Coord]bool{}
	for _, row := range rows {
		rockRowToFullCoords(row, rocks)
	}

	settledSand = simulateSand(rocks, settledSand, false)
	fmt.Println("Answer One:", len(settledSand))

	settledSand = simulateSand(rocks, settledSand, true)
	fmt.Println("Answer Two:", len(settledSand))
}

func rockRowToFullCoords(row string, rocks map[Coord]bool) {
	pathParts := strings.Split(row, "->")
	pathPartsCoords := convertPathPartsToCoords(pathParts)
	addRockLineToRocks(pathPartsCoords, rocks)
}

func convertPathPartsToCoords(pathParts []string) []Coord {
	partsCoords := []Coord{}
	for _, part := range pathParts {
		splitPart := strings.Split(part, ",")
		intX, _ := strconv.Atoi(strings.TrimSpace(splitPart[0]))
		intY, _ := strconv.Atoi(strings.TrimSpace(splitPart[1]))
		partsCoords = append(partsCoords, Coord{x: intX, y: intY})
	}

	return partsCoords
}

func addRockLineToRocks(pathPartsCoords []Coord, rocks map[Coord]bool) {
	for index, coords := range pathPartsCoords {
		rocks[coords] = true
		if index == len(pathPartsCoords)-1 {
			return
		}

		nextPart := pathPartsCoords[index+1]
		direction := determineDirectionOfPath(coords, nextPart)
		currentCoord := Coord{x: coords.x, y: coords.y}
		for currentCoord.x != nextPart.x || currentCoord.y != nextPart.y {
			currentCoord.x = currentCoord.x + direction.x
			currentCoord.y = currentCoord.y + direction.y
			rocks[currentCoord] = true
		}
	}
}

func determineDirectionOfPath(start Coord, end Coord) Coord {
	if start.x < end.x {
		return Coord{x: 1, y: 0}
	}

	if start.x > end.x {
		return Coord{x: -1, y: 0}
	}

	if start.y < end.y {
		return Coord{x: 0, y: 1}
	}

	return Coord{x: 0, y: -1}
}

func simulateSand(rocks map[Coord]bool, settledSand map[Coord]bool, isPartTwo bool) map[Coord]bool {
	endReached := false
	for !endReached {
		endReached = dropSand(rocks, settledSand, isPartTwo)
	}

	return settledSand
}

func dropSand(rocks map[Coord]bool, sand map[Coord]bool, isPartTwo bool) bool {
	maxY := determineMaxY(rocks, isPartTwo)
	sandStart := Coord{x: 500, y: 0}
	currentPosition := sandStart
	for {

		if isPartTwo {
			if currentPosition.y == maxY {
				sand[currentPosition] = true
				return false
			}
		} else {
			if currentPosition.y >= maxY {
				break
			}
		}

		down := Coord{x: currentPosition.x, y: currentPosition.y + 1}
		if !rocks[down] && !sand[down] {
			currentPosition = down
			continue
		}

		left := Coord{x: currentPosition.x - 1, y: currentPosition.y + 1}
		if !rocks[left] && !sand[left] {
			currentPosition = left
			continue
		}

		right := Coord{x: currentPosition.x + 1, y: currentPosition.y + 1}
		if !rocks[right] && !sand[right] {
			currentPosition = right
			continue
		}

		sand[currentPosition] = true
		break
	}

	if isPartTwo {
		if currentPosition.x == sandStart.x && currentPosition.y == sandStart.y {
			return true
		} else {
			return false
		}
	}
	return currentPosition.y == maxY
}

func determineMaxY(rocks map[Coord]bool, isPartTwo bool) int {
	maxY := 0
	for rock := range rocks {
		if rock.y > maxY {
			maxY = rock.y
		}
	}
	if isPartTwo {
		return maxY + 1
	} else {
		return maxY
	}
}
