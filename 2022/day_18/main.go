package main

import (
	"fmt"
	"math"
	"os"
	"strconv"
	"strings"
)

type Position struct {
	x int
	y int
	z int
}

type Cube struct {
	position        Position
	neighbourCoords []Position
	exposedSides    int
}

type Boundary struct {
	minValues Position
	maxValues Position
}

func main() {
	file, _ := os.ReadFile("input.txt")
	cubeStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	cubes, cubePositions := parseCubeStrs(cubeStrs)
	exposedSides := 0
	for _, cube := range cubes {
		cube.calcExposedSides(cubePositions)
		exposedSides += cube.exposedSides
	}
	fmt.Println("Answer One:", exposedSides)

	boundary := calcBoundary(cubes)
	steamPositions := mapSteam(cubePositions, boundary)
	steamCount := 0
	for _, cube := range cubes {
		for _, neighbour := range cube.neighbourCoords {
			if steamPositions[neighbour] {
				steamCount++
			}
		}
	}
	fmt.Println("Answer Two:", steamCount)
}

func parseCubeStrs(cubeStrs []string) ([]Cube, map[Position]bool) {
	cubePositions := map[Position]bool{}
	cubes := []Cube{}
	for _, cubeStr := range cubeStrs {
		coords := strings.Split(cubeStr, ",")
		x, _ := strconv.Atoi(coords[0])
		y, _ := strconv.Atoi(coords[1])
		z, _ := strconv.Atoi(coords[2])

		position := Position{x, y, z}
		cube := Cube{position: position}
		cubePositions[position] = true
		cube.neighbourCoords = calcNeighbours(cube.position.x, cube.position.y, cube.position.z)
		cubes = append(cubes, cube)
	}

	return cubes, cubePositions
}

func calcNeighbours(x int, y int, z int) []Position {
	return []Position{
		{x: x + 1, y: y, z: z},
		{x: x - 1, y: y, z: z},
		{x: x, y: y + 1, z: z},
		{x: x, y: y - 1, z: z},
		{x: x, y: y, z: z + 1},
		{x: x, y: y, z: z - 1},
	}
}

func (cube *Cube) calcExposedSides(cubePositions map[Position]bool) {
	cube.exposedSides = 6
	for _, neighbour := range cube.neighbourCoords {
		if cubePositions[neighbour] {
			cube.exposedSides--
		}
	}
}

func calcBoundary(cubes []Cube) Boundary {
	minX, minY, minZ := math.MaxInt, math.MaxInt, math.MaxInt
	maxX, maxY, maxZ := math.MinInt, math.MinInt, math.MinInt
	for _, cube := range cubes {
		if cube.position.x < minX {
			minX = cube.position.x
		}
		if cube.position.x > maxX {
			maxX = cube.position.x
		}
		if cube.position.y < minY {
			minY = cube.position.y
		}
		if cube.position.y > maxY {
			maxY = cube.position.y
		}
		if cube.position.z < minZ {
			minZ = cube.position.z
		}
		if cube.position.z > maxZ {
			maxZ = cube.position.z
		}
	}

	return Boundary{
		minValues: Position{minX - 1, minY - 1, minZ - 1},
		maxValues: Position{maxX + 1, maxY + 1, maxZ + 1},
	}
}

func mapSteam(cubePositions map[Position]bool, boundary Boundary) map[Position]bool {
	steamPositions := map[Position]bool{}

	seen := map[Position]bool{}
	queue := []Position{boundary.minValues}
	for len(queue) > 0 {
		position := queue[0]
		queue = queue[1:]
		if seen[position] {
			continue
		}
		neighbours := calcNeighbours(position.x, position.y, position.z)
		for _, neighbour := range neighbours {
			if isOutsideBoundary(neighbour, boundary) {
				continue
			}
			if cubePositions[neighbour] || seen[neighbour] {
				continue
			}
			steamPositions[neighbour] = true
			queue = append(queue, neighbour)
		}
		seen[position] = true
	}

	return steamPositions
}

func isOutsideBoundary(position Position, boundary Boundary) bool {
	if position.x < boundary.minValues.x || position.x > boundary.maxValues.x {
		return true
	}
	if position.y < boundary.minValues.y || position.y > boundary.maxValues.y {
		return true
	}
	if position.z < boundary.minValues.z || position.z > boundary.maxValues.z {
		return true
	}

	return false
}
