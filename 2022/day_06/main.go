package main

import (
	"errors"
	"fmt"
	"log"
	"os"
)

func main() {
	file, err := os.ReadFile("input.txt")
	if err != nil {
		log.Fatal(err)
	}

	datastream := string(file)
	answerOne, err := uniqueLettersInWindow(datastream, 4)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Answer One: %d\n", answerOne)

	answerTwo, err := uniqueLettersInWindow(datastream, 14)
	if err != nil {
		log.Fatal(err)
	}
	fmt.Printf("Answer Two: %d\n", answerTwo)
}

func uniqueLettersInWindow(datastream string, windowSize int) (int, error) {
	lowIndex := 0
	highIndex := windowSize - 1
	datastreamLength := len(datastream)
	for highIndex < datastreamLength {
	windowStart:
		for i := lowIndex; i <= highIndex; i++ {
			for j := i + 1; j <= highIndex; j++ {
				if datastream[i] == datastream[j] {
					lowIndex = i + 1
					highIndex = i + windowSize
					continue windowStart
				}
			}
		}
		return highIndex + 1, nil
	}
	return -1, errors.New("Failed to find unique window")
}
