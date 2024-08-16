package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Monkey struct {
	monkeyA   interface{}
	monkeyB   interface{}
	yell      func(monkeys map[string]*Monkey) int
	value     int
	hasYelled bool
}

func main() {
	file, _ := os.ReadFile("input.txt")
	monkeyStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	monkeys := createMonkeys(monkeyStrs)
	rootValue := simulateMonkeys(monkeys)
	fmt.Println("Answer One:", rootValue)
}

func createMonkeys(monkeyStrs []string) map[string]*Monkey {
	monkeys := parseMonkeys(monkeyStrs)
	connectMonkeys(monkeys)

	return monkeys
}

func parseMonkeys(monkeyStrs []string) map[string]*Monkey {
	monkeys := map[string]*Monkey{}
	for _, monkeyStr := range monkeyStrs {
		howlerRe := regexp.MustCompile(`(.+): (-?\d+)`)
		match := howlerRe.FindStringSubmatch(monkeyStr)
		if match != nil {
			name := match[1]
			value, _ := strconv.Atoi(match[2])
			yell := func(monkeys map[string]*Monkey) int { return value }
			monkeys[name] = &Monkey{yell: yell}
			continue
		}

		mathMonkeyRe := regexp.MustCompile(`(.+): (\w+) ([+\-*/]) (\w+)`)
		match = mathMonkeyRe.FindStringSubmatch(monkeyStr)
		name := match[1]
		monkeyAName := match[2]
		monkeyBName := match[4]
		yell := func(monkeys map[string]*Monkey) int {
			a := monkeys[monkeyAName].value
			b := monkeys[monkeyBName].value
			operator := match[3]
			if operator == "+" {
				return a + b
			} else if operator == "-" {
				return a - b
			} else if operator == "*" {
				return a * b
			} else {
				return a / b
			}
		}
		monkeys[name] = &Monkey{monkeyA: monkeyAName, monkeyB: monkeyBName, yell: yell}
	}

	return monkeys
}

func connectMonkeys(monkeys map[string]*Monkey) {
	for _, monkey := range monkeys {
		if monkey.monkeyA != "" {
			if nameA, ok := monkey.monkeyA.(string); ok {
				monkey.monkeyA = monkeys[nameA]
			}
			if nameB, ok := monkey.monkeyB.(string); ok {
				monkey.monkeyB = monkeys[nameB]
			}
		}
	}
}

func simulateMonkeys(monkeys map[string]*Monkey) int {
	for {
		for name, monkey := range monkeys {
			if monkey.hasYelled {
				continue
			}
			if monkeyA, ok := monkey.monkeyA.(*Monkey); ok {
				if !monkeyA.hasYelled {
					continue
				}
			}
			if monkeyB, ok := monkey.monkeyB.(*Monkey); ok {
				if !monkeyB.hasYelled {
					continue
				}
			}

			monkey.value = monkey.yell(monkeys)
			monkey.hasYelled = true
			if name == "root" {
				return monkey.value
			}
		}
	}
}
