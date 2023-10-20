package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strings"
)

type Strategy struct {
	opponentsMove string
	playerMove    string
}

type PlayerMove struct {
	matchesWith string
	beats       string
	pointValue  int
}

func partOne(rounds []Strategy) int {
	moves := map[string]PlayerMove{
		"X": {matchesWith: "A", beats: "C", pointValue: 1},
		"Y": {matchesWith: "B", beats: "A", pointValue: 2},
		"Z": {matchesWith: "C", beats: "B", pointValue: 3},
	}
	totalPoints := 0
	for _, round := range rounds {
		move := moves[round.playerMove]
		if move.matchesWith == round.opponentsMove {
			totalPoints += move.pointValue + 3
		} else if move.beats == round.opponentsMove {
			totalPoints += move.pointValue + 6
		} else {
			totalPoints += move.pointValue
		}
	}

	return totalPoints
}

func partTwo(rounds []Strategy) int {
	opponentsMoveToPoints := map[string]map[string]int{
		"A": {"X": 3, "Y": 4, "Z": 8},
		"B": {"X": 1, "Y": 5, "Z": 9},
		"C": {"X": 2, "Y": 6, "Z": 7},
	}
	totalPoints := 0
	for _, round := range rounds {
		totalPoints += opponentsMoveToPoints[round.opponentsMove][round.playerMove]
	}

	return totalPoints
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	rounds := []Strategy{}
	scanner := bufio.NewScanner(file)
	for scanner.Scan() {
		moves := strings.Split(scanner.Text(), " ")
		round := Strategy{opponentsMove: moves[0], playerMove: moves[1]}
		rounds = append(rounds, round)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	answerOne := partOne(rounds)
	fmt.Printf("Answer One: %d\n", answerOne)

	answerTwo := partTwo(rounds)
	fmt.Printf("Answer Two: %d\n", answerTwo)
}
