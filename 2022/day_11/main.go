package main

import (
	"fmt"
	"os"
	"slices"
	"strconv"
	"strings"
)

type Monkey struct {
	items         []int
	operator      string
	value         string
	testDivisor   int
	tossToOnTrue  int
	tossToOnFalse int
	inspected     int
}

func tossItems(monkey *Monkey, monkeys []Monkey, divisor int) {
	for _, item := range monkey.items {
		monkey.inspected++

		var value int
		if monkey.value == "old" {
			value = item
		} else {
			value, _ = strconv.Atoi(monkey.value)
		}
		switch monkey.operator {
		case "+":
			item += value
		case "*":
			item *= value
		}

		if divisor == 0 {
			item /= 3
		} else {
			item = item % divisor
		}

		var tossTo int
		if (item % monkey.testDivisor) == 0 {
			tossTo = monkey.tossToOnTrue
		} else {
			tossTo = monkey.tossToOnFalse
		}

		monkeys[tossTo].items = append(monkeys[tossTo].items, item)
	}

	monkey.items = []int{}
}

func createMonkey(monkeyBlock string) Monkey {
	lines := strings.Split(monkeyBlock, "\n")

	items := []int{}
	unparsedItems := strings.Split(lines[1][18:], ", ")
	for _, item := range unparsedItems {
		worryLevel, _ := strconv.Atoi(item)
		items = append(items, worryLevel)
	}

	operator := string(lines[2][23])
	value := string(lines[2][25:])

	testDivisor, _ := strconv.Atoi(lines[3][21:])

	tossToOnTrue, _ := strconv.Atoi(lines[4][29:])
	tossToOnFalse, _ := strconv.Atoi(lines[5][30:])

	return Monkey{
		items,
		operator,
		value,
		testDivisor,
		tossToOnTrue,
		tossToOnFalse,
		0,
	}
}

func main() {
	file, _ := os.ReadFile("input.txt")
	unparsedMonkeys := strings.Split(string(file), "\n\n")
	monkeys := []Monkey{}
	for _, monkeyInfo := range unparsedMonkeys {
		monkeys = append(monkeys, createMonkey(monkeyInfo))
	}

	monkeyCopy := append([]Monkey{}, monkeys...)

	for round := 0; round < 20; round++ {
		for i := range monkeys {
			tossItems(&monkeys[i], monkeys, 0)
		}
	}

	inspections := []int{}
	for _, monkey := range monkeys {
		inspections = append(inspections, monkey.inspected)
	}
	slices.Sort(inspections)
	slices.Reverse(inspections)

	fmt.Println("Answer One:", inspections[0]*inspections[1])

	// To stop the 'worry levels' blowing up and causing integer overflows
	// we can mod by the product of the monkeys 'testDivisors'
	divisor := 1
	for _, monkey := range monkeys {
		divisor *= monkey.testDivisor
	}

	monkeys = monkeyCopy

	for round := 0; round < 10000; round++ {
		for i := range monkeys {
			tossItems(&monkeys[i], monkeys, divisor)
		}
	}

	inspections = []int{}
	for _, monkey := range monkeys {
		inspections = append(inspections, monkey.inspected)
	}
	slices.Sort(inspections)
	slices.Reverse(inspections)

	fmt.Println("Answer Two:", inspections[0]*inspections[1])
}
