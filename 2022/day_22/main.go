package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Position struct {
	x int
	y int
}

type Path struct {
	positions map[Position]string
	maxY      int
	maxX      int
}

func main() {
	file, _ := os.ReadFile("input.txt")
	pathAndTurns := strings.Split(strings.Trim(string(file), "\n"), "\n\n")
	initialPath := createPath(pathAndTurns[0])
	path := createDeepCopyOfPath(initialPath)
	instructions := parseInstructions(pathAndTurns[1])
	finalPosition, finalFacing := followPath(path, instructions)
	row := (path.maxY - finalPosition.y) + 1
	col := finalPosition.x + 1

	facingToVal := map[string]int{
		">": 0,
		"v": 1,
		"<": 2,
		"^": 3,
	}
	facingVal := facingToVal[finalFacing]
	password := (row * 1000) + (col * 4) + facingVal
	fmt.Println("Answer One:", password)
}

func createPath(pathStr string) Path {
	path := Path{}
	positions := map[Position]string{}
	rows := strings.Split(pathStr, "\n")
	idx := len(rows) - 1
	path.maxY = idx
	y := 0
	for idx >= 0 {
		row := rows[idx]
		for x, char := range row {
			charStr := string(char)
			if charStr == " " {
				continue
			}
			position := Position{x, y}
			if position.x > path.maxX {
				path.maxX = position.x
			}
			positions[position] = charStr
		}
		idx--
		y++
	}

	path.positions = positions
	return path
}

func createDeepCopyOfPath(path Path) Path {
	pathCopy := path
	pathCopy.positions = make(map[Position]string)
	for k, v := range path.positions {
		pathCopy.positions[k] = v
	}

	return pathCopy
}

func printPath(path Path) {
	y := path.maxY
	for y >= 0 {
		x := 0
		row := ""
		for x <= path.maxX {
			pathChar := path.positions[Position{x, y}]
			if pathChar != "" {
				row += pathChar
			} else {
				row += " "
			}
			x++
		}
		fmt.Println(row)
		y--
	}
}

func parseInstructions(instructionsStr string) []interface{} {
	var instructions []interface{}
	currNumStr := ""
	for idx, char := range instructionsStr {
		charStr := string(char)
		if charStr == "L" || charStr == "R" {
			if len(currNumStr) != 0 {
				num, _ := strconv.Atoi(currNumStr)
				instructions = append(instructions, num)
				currNumStr = ""
			}
			instructions = append(instructions, charStr)
		} else {
			currNumStr += charStr
			if idx == len(instructionsStr)-1 {
				num, _ := strconv.Atoi(currNumStr)
				instructions = append(instructions, num)
			}
		}
	}

	return instructions
}

func followPath(path Path, instructions []interface{}) (Position, string) {
	facing := complex(1, 0)
	currentFacingIcon := directionIcon(facing)
	position := findStartForY(path, path.maxY)
	for _, instruction := range instructions {
		path.positions[position] = currentFacingIcon

		if instruction == "L" {
			facing = turnLeft(facing)
			currentFacingIcon = directionIcon(facing)
		}
		if instruction == "R" {
			facing = turnRight(facing)
			currentFacingIcon = directionIcon(facing)
		}
		if numSteps, ok := instruction.(int); ok {
			facingXDelta := int(real(facing))
			facingYDelta := int(imag(facing))
			for numSteps > 0 {
				nextStepPos := Position{position.x + facingXDelta, position.y + facingYDelta}
				if path.positions[nextStepPos] == "#" {
					break
				}
				numSteps--

				if path.positions[nextStepPos] != "" {
					position = Position{nextStepPos.x, nextStepPos.y}
					path.positions[position] = currentFacingIcon
					continue
				}

				if currentFacingIcon == ">" {
					nextStepPos = findStartForY(path, position.y)
				} else if currentFacingIcon == "<" {
					nextStepPos = findEndForY(path, position.y)
				} else if currentFacingIcon == "^" {
					nextStepPos = findStartForX(path, position.x)
				} else {
					nextStepPos = findEndForX(path, position.x)
				}
				if path.positions[nextStepPos] == "#" {
					break
				}
				position = nextStepPos
				path.positions[position] = currentFacingIcon
			}
		}
	}

	return position, currentFacingIcon
}

func directionIcon(facing complex128) string {
	x, y := real(facing), imag(facing)
	if x == 1 && y == 0 {
		return ">"
	}
	if x == -1 && y == 0 {
		return "<"
	}
	if x == 0 && y == 1 {
		return "^"
	}
	return "v"
}

func findStartForY(path Path, y int) Position {
	x := 0
	for {
		position := Position{x, y}
		if path.positions[position] != "" {
			return position
		}
		x++
	}
}

func findEndForY(path Path, y int) Position {
	x := path.maxX
	for {
		position := Position{x, y}
		if path.positions[position] != "" {
			return position
		}
		x--
	}
}

func findStartForX(path Path, x int) Position {
	y := 0
	for {
		position := Position{x, y}
		if path.positions[position] != "" {
			return position
		}
		y++
	}
}

func findEndForX(path Path, x int) Position {
	y := path.maxY
	for {
		position := Position{x, y}
		if path.positions[position] != "" {
			return position
		}
		y--
	}
}

func turnLeft(facing complex128) complex128 {
	return facing * complex(0, 1)
}

func turnRight(facing complex128) complex128 {
	return facing * complex(0, -1)
}
