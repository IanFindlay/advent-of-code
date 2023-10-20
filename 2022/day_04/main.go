package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type ElfPair struct {
	oneStart int
	oneEnd   int
	twoStart int
	twoEnd   int
}

func partOne(elfPairs []ElfPair) int {
	numCompleteOverlaps := 0
	for _, pair := range elfPairs {
		if pair.oneStart <= pair.twoStart && pair.oneEnd >= pair.twoEnd {
			numCompleteOverlaps++
		} else if pair.twoStart <= pair.oneStart && pair.twoEnd >= pair.oneEnd {
			numCompleteOverlaps++
		}
	}
	return numCompleteOverlaps
}

func partTwo(elfPairs []ElfPair) int {
	numOverlaps := 0
	for _, pair := range elfPairs {
		oneSet := map[int]bool{}
		for i := pair.oneStart; i <= pair.oneEnd; i++ {
			oneSet[i] = true
		}

		for i := pair.twoStart; i <= pair.twoEnd; i++ {
			if oneSet[i] {
				numOverlaps++
				break
			}
		}
	}
	return numOverlaps
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	elfPairs := []ElfPair{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		elves := strings.Split(line, ",")
		elfOneRanges := strings.Split(elves[0], "-")
		elfTwoRanges := strings.Split(elves[1], "-")
		oneStart, err := strconv.Atoi(elfOneRanges[0])
		if err != nil {
			log.Fatal(err)
		}
		oneEnd, err := strconv.Atoi(elfOneRanges[1])
		if err != nil {
			log.Fatal(err)
		}
		twoStart, err := strconv.Atoi(elfTwoRanges[0])
		if err != nil {
			log.Fatal(err)
		}
		twoEnd, err := strconv.Atoi(elfTwoRanges[1])
		if err != nil {
			log.Fatal(err)
		}
		elfPairs = append(elfPairs, ElfPair{oneStart, oneEnd, twoStart, twoEnd})
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	answerOne := partOne(elfPairs)
	fmt.Printf("Answer One: %d\n", answerOne)

	answerTwo := partTwo(elfPairs)
	fmt.Printf("Answer Two: %d\n", answerTwo)
}
