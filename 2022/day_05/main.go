package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"slices"
	"strconv"
	"strings"
)

type Move struct {
	numToMove int
	fromStack int
	toStack   int
}

func pop(alist *[]string) string {
	lenMinusOne := len(*alist) - 1
	poppedValue := (*alist)[lenMinusOne]
	*alist = (*alist)[:lenMinusOne]
	return poppedValue
}

func topCrates(stacks [9][]string) string {
	topCrates := []string{}
	for _, stack := range stacks {
		topCrates = append(topCrates, stack[len(stack)-1])
	}
	return strings.Join(topCrates, "")
}

func partOne(stacks [9][]string, moves []Move) string {
	for _, move := range moves {
		for i := 0; i < move.numToMove; i++ {
			popped := pop(&stacks[move.fromStack])
			stacks[move.toStack] = append(stacks[move.toStack], popped)
		}
	}
	return topCrates(stacks)

}

func partTwo(stacks [9][]string, moves []Move) string {
	for _, move := range moves {
		from := stacks[move.fromStack]
		to := stacks[move.toStack]
		toMove := from[len(from)-move.numToMove:]
		stacks[move.fromStack] = from[:len(from)-move.numToMove]
		stacks[move.toStack] = append(to, toMove...)
	}

	return topCrates(stacks)
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	stacks := [9][]string{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		line := scanner.Text()
		if string(line[1]) == "1" {
			break
		} else {
			charIndexes := [9]int{1, 5, 9, 13, 17, 21, 25, 29, 33}
			for i := 0; i < 9; i++ {
				crate := string(line[charIndexes[i]])
				if crate != " " {
					stacks[i] = append(stacks[i], string(line[charIndexes[i]]))
				}
			}
		}
	}
	for _, stack := range stacks {
		slices.Reverse(stack)
	}

	moves := []Move{}
	for scanner.Scan() {
		line := scanner.Text()
		if line == "" {
			continue
		}
		lineSplit := strings.Split(line, " ")
		numToMove, err := strconv.Atoi(lineSplit[1])
		if err != nil {
			log.Fatal(err)
		}
		fromStack, err := strconv.Atoi(lineSplit[3])
		if err != nil {
			log.Fatal(err)
		}
		toStack, err := strconv.Atoi(lineSplit[5])
		if err != nil {
			log.Fatal(err)
		}
		move := Move{numToMove, fromStack - 1, toStack - 1}
		moves = append(moves, move)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	stacksCopy := [9][]string{}
	for i, stack := range stacks {
		stackCopy := make([]string, len(stack))
		copy(stackCopy, stack)
		stacksCopy[i] = stackCopy
	}

	answerOne := partOne(stacksCopy, moves)
	fmt.Printf("Answer One: %s\n", answerOne)

	answerTwo := partTwo(stacks, moves)
	fmt.Printf("Answer Two: %s\n", answerTwo)
}
