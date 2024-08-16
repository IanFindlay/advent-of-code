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
	z int
}

type Cube struct {
	position        Position
	neighbourCoords []Position
	exposedSides    int
}

type CubeMethods interface {
	calcNeighbours()
	calcExposedSides(map[Position]bool)
}

func main() {
	file, _ := os.ReadFile("test-input.txt")
	cubeStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	cubes, cubePositions := parseCubeStrs(cubeStrs)
	exposedSides := 0
	for _, cube := range cubes {
		cube.calcExposedSides(cubePositions)
		exposedSides += cube.exposedSides
	}

	fmt.Println("Answer One:", exposedSides)
}

func parseCubeStrs(cubeStrs []string) ([]*Cube, map[Position]bool) {
	cubePositions := map[Position]bool{}
	cubes := []*Cube{}
	for _, cubeStr := range cubeStrs {
		coords := strings.Split(cubeStr, ",")
		x, _ := strconv.Atoi(coords[0])
		y, _ := strconv.Atoi(coords[1])
		z, _ := strconv.Atoi(coords[2])

		position := Position{x, y, z}
		cube := Cube{position: position}
		cubePositions[position] = true
		cube.calcNeighbourCoords()
		cubes = append(cubes, &cube)
	}

	return cubes, cubePositions
}

func (cube *Cube) calcNeighbourCoords() {
	x := cube.position.x
	y := cube.position.y
	z := cube.position.z

	cube.neighbourCoords = []Position{
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
