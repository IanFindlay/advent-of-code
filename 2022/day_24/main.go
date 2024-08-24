package main

import (
	"fmt"
	"os"
	"strings"
)

type basin struct {
	basinMap       map[point]bool
	blizzards      map[point]string
	blizzardsByMin map[int]map[point]bool
	start          point
	end            point
	maxCoords      point
}

type point struct {
	x int
	y int
}

type queue []point

type cacheKey struct {
	position point
	blizzMod int
}

type bfsInfo struct {
	minutes    int
	startPoint point
	endPoint   point
}

func main() {
	file, _ := os.ReadFile("input.txt")
	rows := strings.Split(strings.TrimSpace(string(file)), "\n")
	basin := createBasin(rows)
	basin.genAllBlizzards()
	partOne := basin.bfs(bfsInfo{0, basin.start, basin.end})
	fmt.Println("Answer One:", partOne.minutes)

	backToStart := basin.bfs(partOne)
	partTwo := basin.bfs(backToStart)
	fmt.Println("Answer Two:", partTwo.minutes)
}

func createBasin(rows []string) basin {
	basinMap := make(map[point]bool)
	start := point{}
	end := point{}
	blizzardChars := map[string]bool{"<": true, ">": true, "v": true, "^": true}
	blizzards := make(map[point]string)
	maxRowIdx := len(rows) - 1
	y := maxRowIdx
	for _, row := range rows {
		for x, r := range row {
			char := string(r)
			if char == "#" {
				continue
			}
			position := point{x, y}
			basinMap[position] = true
			if y == maxRowIdx && char == "." {
				start = position
			} else if y == 0 && char == "." {
				end = position
			}

			if blizzardChars[char] {
				blizzards[position] = char
			}
		}
		y--
	}

	maxCoords := point{len(rows[0]) - 1, len(rows) - 1}
	blizzardsByMin := make(map[int]map[point]bool)

	return basin{basinMap, blizzards, blizzardsByMin, start, end, maxCoords}
}

func (basin basin) genAllBlizzards() {
	blizzsAtTimeZero := make(map[point]bool)
	for pos := range basin.blizzards {
		blizzsAtTimeZero[pos] = true
	}
	basin.blizzardsByMin[0] = blizzsAtTimeZero
	lcm := basin.lowestCommonMultiple()
	for position, dir := range basin.blizzards {
		basin.blizzPointByMinUpToLCM(position, dir, lcm)
	}
}

func (basin basin) lowestCommonMultiple() int {
	a, b := basin.maxCoords.x-1, basin.maxCoords.y-1
	for b != 0 {
		a, b = b, a%b
	}

	return ((basin.maxCoords.x - 1) * (basin.maxCoords.y - 1)) / a
}

func (basin basin) blizzPointByMinUpToLCM(pos point, dir string, lcm int) {
	currPos := pos
	for idx := 1; idx < lcm; idx++ {
		if _, exist := basin.blizzardsByMin[idx]; !exist {
			basin.blizzardsByMin[idx] = make(map[point]bool)
		}
		x, y := currPos.x, currPos.y
		switch dir {
		case "<":
			if x == 1 {
				x = basin.maxCoords.x - 1
			} else {
				x--
			}
		case ">":
			if x == basin.maxCoords.x-1 {
				x = 1
			} else {
				x++
			}
		case "^":
			if y == basin.maxCoords.y-1 {
				y = 1
			} else {
				y++
			}
		case "v":
			if y == 1 {
				y = basin.maxCoords.y - 1
			} else {
				y--
			}
		}
		currPos = point{x, y}
		basin.blizzardsByMin[idx][currPos] = true
	}
}

func (basin basin) bfs(info bfsInfo) bfsInfo {
	visited := make(map[cacheKey]bool)
	numUniqueBlizzConfigs := len(basin.blizzardsByMin)
	nodes := queue{}
	nodes.enqueue(info.startPoint)
	minute := info.minutes
	for !nodes.isEmpty() {
		numNodesAtStep := len(nodes)
		for i := 0; i < numNodesAtStep; i++ {
			node := nodes.dequeue()
			nodeCacheKey := cacheKey{node, minute}
			if visited[nodeCacheKey] {
				continue
			}
			visited[nodeCacheKey] = true

			nextBlizzMod := (minute + 1) % numUniqueBlizzConfigs
			nextMoves := node.getMoves(basin, nextBlizzMod)
			for _, move := range nextMoves {
				nextNodeCacheKey := cacheKey{move, nextBlizzMod}
				if visited[nextNodeCacheKey] {
					continue
				}

				if move == info.endPoint {
					return bfsInfo{
						minutes:    minute + 1,
						startPoint: info.endPoint,
						endPoint:   info.startPoint,
					}
				}

				nodes.enqueue(move)
			}
		}
		minute++
	}

	return info
}

func (q *queue) isEmpty() bool {
	return len(*q) == 0
}

func (q *queue) enqueue(qi point) {
	*q = append(*q, qi)
}

func (q *queue) dequeue() point {
	qi := (*q)[0]
	*q = (*q)[1:]
	return qi
}

func (item *point) getMoves(basin basin, nextBlizzMod int) []point {
	x, y := item.x, item.y
	potentialSteps := []point{
		{x + 1, y},
		{x - 1, y},
		{x, y + 1},
		{x, y - 1},
		{x, y},
	}

	validSteps := []point{}
	for _, step := range potentialSteps {
		if !basin.basinMap[step] {
			continue
		}
		if basin.blizzardsByMin[nextBlizzMod][step] {
			continue
		}
		validSteps = append(validSteps, step)
	}

	return validSteps
}
