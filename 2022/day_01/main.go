package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
    "slices"
)

func getCalorieTotals(lines []string) []int {
    if len(lines) == 0 {
        return []int{}
    }
	totalCalories := []int{0}

	numElves := 0
	for _, line := range lines {
		if line == "" {
			totalCalories = append(totalCalories, 0)
			numElves += 1
		}
		calories, err := strconv.Atoi(line)
		if err == nil {
			totalCalories[numElves] += calories
		}
	}

	return totalCalories
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	lines := []string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	calorieTotals := getCalorieTotals(lines)
	slices.Sort(calorieTotals)

	fmt.Printf("Answer One: %d\n", calorieTotals[len(calorieTotals)-1])

	topThreeCalorieTotals := calorieTotals[len(calorieTotals)-3:]
	topThreeSum := 0
	for _, calories := range topThreeCalorieTotals {
		topThreeSum += calories
	}
	fmt.Printf("Answer Two: %d\n", topThreeSum)
}
