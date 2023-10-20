package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"unicode"
)

type Rucksack struct {
	firstCompartment  string
	secondCompartment string
}

func runeListToPrioritySum(runeList []rune) int {
	prioritySum := 0
	for _, char := range runeList {
		prioritySum += int(char)
		if unicode.IsUpper(char) {
			prioritySum -= 38
		} else {
			prioritySum -= 96
		}
	}

	return prioritySum
}

func partOne(rucksacks []Rucksack) int {
	runeList := []rune{}
	for _, rucksack := range rucksacks {
		oneSet := map[rune]bool{}
		for _, char := range rucksack.firstCompartment {
			oneSet[char] = true
		}
		for _, char := range rucksack.secondCompartment {
			if oneSet[char] {
				runeList = append(runeList, char)
				break
			}
		}
	}

	return runeListToPrioritySum(runeList)
}

func partTwo(rucksacks []Rucksack) int {
	runeList := []rune{}
	i := 0
	for i < len(rucksacks) {
		elfOne := rucksacks[i]
		elfTwo := rucksacks[i+1]
		elfThree := rucksacks[i+2]

		oneSet := map[rune]bool{}
		for _, char := range elfOne.firstCompartment + elfOne.secondCompartment {
			oneSet[char] = true
		}

		oneTwoIntersection := map[rune]bool{}
		for _, char := range elfTwo.firstCompartment + elfTwo.secondCompartment {
			if oneSet[char] {
				oneTwoIntersection[char] = true
			}
		}

		for _, char := range elfThree.firstCompartment + elfThree.secondCompartment {
			if oneTwoIntersection[char] {
				runeList = append(runeList, char)
				break
			}
		}

		i += 3
	}

	return runeListToPrioritySum(runeList)
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	rucksacks := []Rucksack{}
	for scanner.Scan() {
		line := scanner.Text()
		halfway := len(line) / 2
		rucksack := Rucksack{firstCompartment: line[:halfway], secondCompartment: line[halfway:]}
		rucksacks = append(rucksacks, rucksack)
	}
	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	answerOne := partOne(rucksacks)
	fmt.Printf("Answer One: %d\n", answerOne)

	answerTwo := partTwo(rucksacks)
	fmt.Printf("Answer Two: %d\n", answerTwo)
}
