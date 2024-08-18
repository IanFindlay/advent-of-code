package main

import (
	"fmt"
	"os"
	"strings"
)

type Position struct {
	x int
	y int
}

type ElfMap struct {
	elfPositions  map[Position]bool
	intendedMoves map[Position]Position
	maxCoords     Position
	minCoords     Position
	directionIdx  int
}

func main() {
	file, _ := os.ReadFile("input.txt")
	rows := strings.Split(strings.TrimSpace(string(file)), "\n")
	elfMap := createElfMap(rows)
	endMapOne, _ := doRounds(elfMap, 10)
	width := (endMapOne.maxCoords.x - endMapOne.minCoords.x) + 1
	height := (endMapOne.maxCoords.y - endMapOne.minCoords.y) + 1
	emptyTileCount := (width * height) - len(endMapOne.elfPositions)
	fmt.Println("Answer One:", emptyTileCount)

	_, roundsTillEnd := doRounds(elfMap, 10000)
	fmt.Println("Answer Two:", roundsTillEnd)
}

func createElfMap(rows []string) ElfMap {
	elfPositions := make(map[Position]bool)
	idx := len(rows) - 1
	elfMap := ElfMap{
		maxCoords: Position{y: idx},
	}
	y := 0
	for idx >= 0 {
		row := rows[idx]
		for x, char := range row {
			charStr := string(char)
			if charStr == "#" {
				position := Position{x, y}
				elfPositions[position] = true
				if x > elfMap.maxCoords.x {
					elfMap.maxCoords.x = x
				}
			}
		}
		idx--
		y++
	}
	elfMap.elfPositions = elfPositions
	elfMap.intendedMoves = make(map[Position]Position)

	return elfMap
}

func doRounds(elfMap ElfMap, roundLimit int) (ElfMap, int) {
	round := 0
	numElves := len(elfMap.elfPositions)
	for {
		if round == roundLimit {
			return elfMap, round
		}

		isolatedElves := numElves
		elfMap.intendedMoves = make(map[Position]Position)
		for elfPos := range elfMap.elfPositions {
			freeAdjs := checkAdjacent(elfMap, elfPos)
			lenFreeAdjs := len(freeAdjs)
			if lenFreeAdjs == 8 {
				isolatedElves--
			}
		}
		if isolatedElves == 0 {
			return elfMap, round + 1
		}

		assignIntendedMoves(elfMap)
		validMoves := findValidMoves(elfMap)
		newPositions := make(map[Position]bool)
		elfMap.maxCoords = Position{}
		elfMap.minCoords = Position{}
		for elfPos := range elfMap.elfPositions {
			intendedMove := elfMap.intendedMoves[elfPos]
			if !validMoves[intendedMove] {
				intendedMove = elfPos
			}
			newPositions[intendedMove] = true

			if intendedMove.x > elfMap.maxCoords.x {
				elfMap.maxCoords.x = intendedMove.x
			}
			if intendedMove.x < elfMap.minCoords.x {
				elfMap.minCoords.x = intendedMove.x
			}
			if intendedMove.y > elfMap.maxCoords.y {
				elfMap.maxCoords.y = intendedMove.y
			}
			if intendedMove.y < elfMap.minCoords.y {
				elfMap.minCoords.y = intendedMove.y
			}
		}
		elfMap.elfPositions = newPositions
		round++
		elfMap.directionIdx = (elfMap.directionIdx + 1) % 4
	}
}

func checkAdjacent(elfMap ElfMap, position Position) map[string]bool {
	freeAdjs := make(map[string]bool)
	x, y := position.x, position.y
	adjacents := map[string]Position{
		"N":  {x, y + 1},
		"NE": {x + 1, y + 1},
		"E":  {x + 1, y},
		"SE": {x + 1, y - 1},
		"S":  {x, y - 1},
		"SW": {x - 1, y - 1},
		"W":  {x - 1, y},
		"NW": {x - 1, y + 1},
	}
	for key, adjacent := range adjacents {
		if !elfMap.elfPositions[adjacent] {
			freeAdjs[key] = true
		}
	}

	return freeAdjs
}

func assignIntendedMoves(elfMap ElfMap) {
	directions := []string{"N", "S", "W", "E"}
	for elfPos := range elfMap.elfPositions {
		freeAdjs := checkAdjacent(elfMap, elfPos)
		if len(freeAdjs) == 8 {
			elfMap.intendedMoves[elfPos] = elfPos
			continue
		}

		dirsToCheck := 4
		idx := elfMap.directionIdx
		intendedMove := elfPos
		for dirsToCheck > 0 {
			dirToCheck := directions[idx]
			if dirToCheck == "N" {
				if freeAdjs["N"] && freeAdjs["NE"] && freeAdjs["NW"] {
					intendedMove = Position{x: elfPos.x, y: elfPos.y + 1}
					break
				}
			} else if dirToCheck == "S" {
				if freeAdjs["S"] && freeAdjs["SW"] && freeAdjs["SE"] {
					intendedMove = Position{x: elfPos.x, y: elfPos.y - 1}
					break
				}
			} else if dirToCheck == "W" {
				if freeAdjs["W"] && freeAdjs["NW"] && freeAdjs["SW"] {
					intendedMove = Position{x: elfPos.x - 1, y: elfPos.y}
					break
				}
			} else if dirToCheck == "E" {
				if freeAdjs["E"] && freeAdjs["NE"] && freeAdjs["SE"] {
					intendedMove = Position{x: elfPos.x + 1, y: elfPos.y}
					break
				}
			}
			idx = (idx + 1) % 4
			dirsToCheck--
		}
		elfMap.intendedMoves[elfPos] = intendedMove
	}
}

func findValidMoves(elfMap ElfMap) map[Position]bool {
	validMoves := make(map[Position]bool)
	positionCounts := make(map[Position]int)
	for _, position := range elfMap.intendedMoves {
		positionCounts[position] = positionCounts[position] + 1
	}

	for position, count := range positionCounts {
		if count <= 1 {
			validMoves[position] = true
		}
	}

	return validMoves
}
