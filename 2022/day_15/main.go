package main

import (
	"fmt"
	"math"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Coord struct {
	x int
	y int
}

type Report struct {
	sensor        Coord
	closestBeacon Coord
	distance      int
}

func main() {
	file, _ := os.ReadFile("input.txt")
	reports := strings.Split(strings.TrimSpace(string(file)), "\n")
	parsedReports, beaconLocations := parseReports(reports)

	minX, maxX := getXRange(parsedReports)
	noBeaconCount := noBeaconsCount(minX, maxX, 2000000, parsedReports, beaconLocations)
	fmt.Println("Answer One:", noBeaconCount)

	hiddenBeaconLocation := Coord{}
	for _, report := range parsedReports {
		beaconFound, beaconCoords := checkPerimeterCoords(report, parsedReports)
		if beaconFound {
			hiddenBeaconLocation = beaconCoords
			break
		}
	}
	frequency := hiddenBeaconLocation.x*4000000 + hiddenBeaconLocation.y
	fmt.Println("Answer Two:", frequency)
}

func parseReports(reports []string) ([]Report, map[Coord]bool) {
	parsedReports := []Report{}
	beaconLocations := map[Coord]bool{}
	re, _ := regexp.Compile(`Sensor at x=(-?\d+), y=(-?\d+): closest beacon is at x=(-?\d+), y=(-?\d+)`)
	for _, report := range reports {
		matches := re.FindStringSubmatch(report)
		sensorX, _ := strconv.Atoi(matches[1])
		sensorY, _ := strconv.Atoi(matches[2])
		beaconX, _ := strconv.Atoi(matches[3])
		beaconY, _ := strconv.Atoi(matches[4])
		distance := calcManDist(sensorX, sensorY, beaconX, beaconY)
		parsedReport := Report{
			sensor:        Coord{x: sensorX, y: sensorY},
			closestBeacon: Coord{x: beaconX, y: beaconY},
			distance:      distance,
		}
		parsedReports = append(parsedReports, parsedReport)
		beaconLocations[parsedReport.closestBeacon] = true
	}

	return parsedReports, beaconLocations
}

func calcManDist(x1 int, y1 int, x2 int, y2 int) int {
	return int(math.Abs(float64(x1-x2)) + math.Abs(float64(y1-y2)))
}

func getXRange(parsedReports []Report) (int, int) {
	minX := math.MaxInt
	maxX := math.MinInt
	for _, report := range parsedReports {
		reportMinX := min(report.sensor.x, report.closestBeacon.x)
		reportMaxX := max(report.sensor.x, report.closestBeacon.x)
		if minX > reportMinX {
			minX = reportMinX
		}
		if maxX < reportMaxX {
			maxX = reportMaxX
		}
	}

	return minX, maxX
}

func noBeaconsCount(startX int, maxX int, y int, reports []Report, beacons map[Coord]bool) int {
	x := startX
	noBeaconCount := 0
	for x <= maxX {
		toCheck := Coord{x: x, y: y}
		x++
		for _, report := range reports {
			manDist := calcManDist(report.sensor.x, report.sensor.y, toCheck.x, toCheck.y)
			if manDist <= report.distance && !beacons[toCheck] {
				noBeaconCount++
				break
			}
		}
	}

	return noBeaconCount
}

// Only need to check perimeter coords as if the beacon existed outside of the perimeters
// of all of the sensor's ranges then there wouldn't be a unique answer
func checkPerimeterCoords(report Report, parsedReports []Report) (bool, Coord) {
	minXY := 0
	maxXY := 4000000
	perimeterDistance := report.distance + 1
	queue := []Coord{report.closestBeacon}
	explored := map[Coord]bool{}
	for len(queue) > 0 {
		currCoord := queue[0]
		queue = queue[1:]
		adjacent := []Coord{
			{x: currCoord.x + 1, y: currCoord.y},
			{x: currCoord.x - 1, y: currCoord.y},
			{x: currCoord.x, y: currCoord.y + 1},
			{x: currCoord.x, y: currCoord.y - 1},
			{x: currCoord.x + 1, y: currCoord.y + 1},
			{x: currCoord.x + 1, y: currCoord.y - 1},
			{x: currCoord.x - 1, y: currCoord.y + 1},
			{x: currCoord.x - 1, y: currCoord.y - 1},
		}

		for _, coord := range adjacent {
			if explored[currCoord] {
				continue
			}
			if coord.x < minXY || coord.x > maxXY {
				continue
			}
			if coord.y < minXY || coord.y > maxXY {
				continue
			}
			distanceToSensor := calcManDist(report.sensor.x, report.sensor.y, coord.x, coord.y)
			if distanceToSensor == perimeterDistance {
				beaconFound := checkForHiddenBeacon(parsedReports, coord)

				if !beaconFound {
					queue = append(queue, coord)
				} else {
					return true, coord
				}
			}
		}
		explored[currCoord] = true
	}

	return false, Coord{}
}

func checkForHiddenBeacon(reports []Report, toCheck Coord) bool {
	for _, report := range reports {
		distanceToSensor := calcManDist(report.sensor.x, report.sensor.y, toCheck.x, toCheck.y)
		if distanceToSensor <= report.distance {
			return false
		}
	}

	return true
}
