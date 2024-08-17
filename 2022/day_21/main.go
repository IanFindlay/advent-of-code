package main

import (
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

type Monkey struct {
	monkeyAName string
	monkeyBName string
	monkeyA     *Monkey
	monkeyB     *Monkey
	operator    string
	yell        func(monkeys map[string]*Monkey) int
	value       int
	hasYelled   bool
}

type TraceInfo struct {
	path  []*Monkey
	isLHS []bool
}

func main() {
	file, _ := os.ReadFile("input.txt")
	monkeyStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	monkeys := createMonkeys(monkeyStrs)
	rootValue := simulateMonkeys(monkeys)
	fmt.Println("Answer One:", rootValue)

	monkeys = createMonkeys(monkeyStrs)
	trace := traceNumThroughSim(monkeys)
	numToYell := calcNumToYell(trace)
	fmt.Println("Answer Two:", numToYell)
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
		operator := match[3]
		monkeyBName := match[4]
		yell := func(monkeys map[string]*Monkey) int {
			a := monkeys[monkeyAName].value
			b := monkeys[monkeyBName].value
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
		monkeys[name] = &Monkey{
			monkeyAName: monkeyAName, monkeyBName: monkeyBName,
			yell: yell, operator: operator}
	}

	return monkeys
}

func connectMonkeys(monkeys map[string]*Monkey) {
	for _, monkey := range monkeys {
		if monkey.monkeyAName != "" {
			monkey.monkeyA = monkeys[monkey.monkeyAName]
			monkey.monkeyB = monkeys[monkey.monkeyBName]
		}
	}
}

func simulateMonkeys(monkeys map[string]*Monkey) int {
	for {
		for name, monkey := range monkeys {
			if monkey.hasYelled {
				continue
			}
			if monkey.monkeyA != nil && !monkey.monkeyA.hasYelled {
				continue
			}
			if monkey.monkeyB != nil && !monkey.monkeyB.hasYelled {
				continue
			}

			monkey.value = monkey.yell(monkeys)
			monkey.hasYelled = true
			if name == "root" {
				return monkey.value
			}
		}
	}
}

func traceNumThroughSim(monkeys map[string]*Monkey) TraceInfo {
	path := []*Monkey{}
	isLHS := []bool{true}
	targetMonkey := monkeys["humn"]
	for {
		for name, monkey := range monkeys {
			if monkey.hasYelled {
				continue
			}

			if monkey.monkeyA != nil {
				if !monkey.monkeyA.hasYelled {
					continue
				}
				if !monkey.monkeyB.hasYelled {
					continue
				}
			}

			monkey.value = monkey.yell(monkeys)
			monkey.hasYelled = true

			if monkey.monkeyA == targetMonkey {
				path = append(path, monkey.monkeyA)
				isLHS = append(isLHS, true)
				targetMonkey = monkeys[name]
			}

			if monkey.monkeyB == targetMonkey {
				path = append(path, monkey.monkeyB)
				isLHS = append(isLHS, false)
				targetMonkey = monkeys[name]
			}

			if name == "root" {
				path = append(path, monkeys["root"])
				return TraceInfo{
					path:  path,
					isLHS: isLHS,
				}
			}
		}
	}
}

// Find number to yell by setting final value of number descended from "humn" to other value
// and working backwards inversing the operations that led to that final number
func calcNumToYell(trace TraceInfo) int {
	monkeys := trace.path
	idx := len(monkeys) - 1
	traceValue := monkeys[idx].monkeyA.value
	if trace.isLHS[idx] {
		traceValue = monkeys[idx].monkeyB.value
	}
	idx--

	for idx > 0 {
		monkey := monkeys[idx]
		if monkey.operator == "+" {
			if trace.isLHS[idx] {
				traceValue -= monkey.monkeyB.value
			} else {
				traceValue -= monkey.monkeyA.value
			}
		}

		if monkey.operator == "-" {
			if trace.isLHS[idx] {
				traceValue += monkey.monkeyB.value
			} else {
				traceValue = monkey.monkeyA.value - traceValue
			}
		}

		if monkey.operator == "*" {
			if trace.isLHS[idx] {
				traceValue /= monkey.monkeyB.value
			} else {
				traceValue /= monkey.monkeyA.value
			}
		}

		if monkey.operator == "/" {
			if trace.isLHS[idx] {
				traceValue *= monkey.monkeyB.value
			} else {
				traceValue = monkey.monkeyA.value / traceValue
			}
		}
		idx--
	}

	return traceValue
}
