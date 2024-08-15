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

type RockPattern struct {
	startingCoords []Coord
	coords         []Coord
	leftEdgeX      int
	rightEdgeX     int
	bottomEdgeY    int
	topEdgeY       int
}

type Rock interface {
	moveUntilSettled([]string, int, map[Coord]bool) int
	moveToStartPosition(int)
	moveDown()
	moveUp()
	moveLeft()
	moveRight()
	checkForCollision(map[Coord]bool) bool
}

type Cache struct {
	rocksSettled int
	maxY         int
}

type CycleInfo struct {
	start      int
	startY     int
	length     int
	yIncrease  int
	maxYValues []int
}

func main() {
	file, _ := os.ReadFile("input.txt")
	jetPattern := strings.Split(strings.TrimSpace(string(file)), "")
	rocks := getRocks()

	unitsTall := simulate2022Rocks(rocks, jetPattern)
	fmt.Println("Answer One:", unitsTall)

	cycleInfo := simulateUntilCycle(rocks, jetPattern)
	finalMaxY := getToEndStateUsingCycle(cycleInfo)
	fmt.Println("Answer Two:", finalMaxY)
}

func getRocks() []RockPattern {
	rocks := []RockPattern{
		{
			startingCoords: []Coord{
				{x: 2, y: 0},
				{x: 3, y: 0},
				{x: 4, y: 0},
				{x: 5, y: 0},
			},
			leftEdgeX:   2,
			rightEdgeX:  5,
			bottomEdgeY: 0,
			topEdgeY:    0,
		},

		{
			startingCoords: []Coord{
				{x: 3, y: 0},
				{x: 2, y: 1},
				{x: 3, y: 1},
				{x: 4, y: 1},
				{x: 3, y: 2},
			},
			leftEdgeX:   2,
			rightEdgeX:  4,
			bottomEdgeY: 0,
			topEdgeY:    2,
		},

		{
			startingCoords: []Coord{
				{x: 2, y: 0},
				{x: 3, y: 0},
				{x: 4, y: 0},
				{x: 4, y: 2},
				{x: 4, y: 1},
			},
			leftEdgeX:   2,
			rightEdgeX:  4,
			bottomEdgeY: 0,
			topEdgeY:    2,
		},

		{
			startingCoords: []Coord{
				{x: 2, y: 0},
				{x: 2, y: 1},
				{x: 2, y: 2},
				{x: 2, y: 3},
			},
			leftEdgeX:   2,
			rightEdgeX:  2,
			bottomEdgeY: 0,
			topEdgeY:    3,
		},

		{
			startingCoords: []Coord{
				{x: 2, y: 0},
				{x: 3, y: 0},
				{x: 2, y: 1},
				{x: 3, y: 1},
			},
			leftEdgeX:   2,
			rightEdgeX:  3,
			bottomEdgeY: 0,
			topEdgeY:    1,
		},
	}

	return rocks
}

func simulate2022Rocks(rocks []RockPattern, jetPattern []string) int {
	settledRocks := map[Coord]bool{}
	maxY := -1
	jetIndex := 0
	rockIndex := 0
	numSettledRocks := 0
	for numSettledRocks < 2022 {
		rock := rocks[rockIndex]
		rock.moveToStartPosition(maxY)
		jetIndex = rock.moveUntilSettled(jetPattern, jetIndex, settledRocks)
		numSettledRocks++
		rockIndex = (rockIndex + 1) % 5
		if rock.topEdgeY > maxY {
			maxY = rock.topEdgeY
		}
	}

	return maxY + 1
}

func (rock *RockPattern) moveToStartPosition(highestY int) {
	yOffset := highestY + 4
	for index := range rock.startingCoords {
		coords := rock.startingCoords[index]
		newY := coords.y + yOffset
		rock.coords = append(rock.coords, Coord{x: coords.x, y: newY})
	}
	rock.bottomEdgeY += yOffset
	rock.topEdgeY += yOffset
}

func (rock *RockPattern) moveUntilSettled(jetPattern []string, jetIndex int, settledRocks map[Coord]bool) int {
	for {
		if jetPattern[jetIndex] == ">" {
			rock.moveRight()
			if rock.collides(settledRocks) {
				rock.moveLeft()
			}
		} else {
			rock.moveLeft()
			if rock.collides(settledRocks) {
				rock.moveRight()
			}
		}

		jetIndex++
		if jetIndex == len(jetPattern) {
			jetIndex = 0
		}

		rock.moveDown()
		if rock.collides(settledRocks) {
			rock.moveUp()
			for _, coord := range rock.coords {
				settledRocks[coord] = true
			}
			break
		}
	}

	return jetIndex
}

func (rock *RockPattern) moveDown() {
	for index := range rock.coords {
		rock.coords[index].y--
	}
	rock.bottomEdgeY--
	rock.topEdgeY--
}

func (rock *RockPattern) moveUp() {
	for index := range rock.coords {
		rock.coords[index].y++
	}
	rock.bottomEdgeY++
	rock.topEdgeY++
}

func (rock *RockPattern) moveLeft() {
	for index := range rock.coords {
		rock.coords[index].x--
	}
	rock.leftEdgeX--
	rock.rightEdgeX--
}

func (rock *RockPattern) moveRight() {
	for index := range rock.coords {
		rock.coords[index].x++
	}
	rock.leftEdgeX++
	rock.rightEdgeX++
}

func (rock *RockPattern) collides(settledRocks map[Coord]bool) bool {
	if rock.leftEdgeX == -1 || rock.rightEdgeX == 7 || rock.bottomEdgeY == -1 {
		return true
	}

	for _, coord := range rock.coords {
		if settledRocks[coord] {
			return true
		}
	}

	return false
}

func simulateUntilCycle(rocks []RockPattern, jetPattern []string) CycleInfo {
	settledRocks := map[Coord]bool{}
	maxY := -1
	colHeights := [7]int{0, 0, 0, 0, 0, 0, 0}
	jetIndex := 0
	rockIndex := 0
	numSettledRocks := 0
	cache := map[string]bool{}
	cacheKeyToCache := map[string]Cache{}
	maxYValues := []int{}
	for {
		rock := rocks[rockIndex]
		rock.moveToStartPosition(maxY)
		jetIndex = rock.moveUntilSettled(jetPattern, jetIndex, settledRocks)
		numSettledRocks++
		rockIndex = (rockIndex + 1) % 5
		if rock.topEdgeY > maxY {
			maxY = rock.topEdgeY
		}
		maxYValues = append(maxYValues, maxY)

		for _, coord := range rock.coords {
			settledHeight := coord.y
			if colHeights[coord.x] < settledHeight {
				colHeights[coord.x] = settledHeight
			}
		}

		cacheList := [9]int{0, 0, 0, 0, 0, 0, 0, 0, 0}
		for index := range colHeights {
			cacheList[index] = maxY - colHeights[index]
		}
		cacheList[7] = rockIndex
		cacheList[8] = jetIndex

		cacheKey := ""
		for _, value := range cacheList {
			cacheKey += strconv.Itoa(value)
		}
		if cache[cacheKey] {
			cacheValues := cacheKeyToCache[cacheKey]
			cycleStart := cacheValues.rocksSettled
			cycleLen := numSettledRocks - cacheValues.rocksSettled
			cycleYChange := maxY - cacheValues.maxY
			startY := cacheValues.maxY
			return CycleInfo{
				start: cycleStart, startY: startY, length: cycleLen,
				yIncrease: cycleYChange, maxYValues: maxYValues,
			}
		}
		cache[cacheKey] = true
		cacheKeyToCache[cacheKey] = Cache{numSettledRocks, maxY}
	}
}

func getToEndStateUsingCycle(cycleInfo CycleInfo) int {
	numRocksToSim := 1000000000000
	simsAfterCycleStart := numRocksToSim - cycleInfo.start
	numCycles := simsAfterCycleStart / cycleInfo.length
	remainingRocks := simsAfterCycleStart - (numCycles * cycleInfo.length)
	yAfterCycles := cycleInfo.startY + (cycleInfo.yIncrease * numCycles)
	finishingIndex := cycleInfo.start + remainingRocks
	yIncreaseFromCycleStartToFinished := cycleInfo.maxYValues[finishingIndex] - cycleInfo.startY
	return yAfterCycles + yIncreaseFromCycleStartToFinished
}
