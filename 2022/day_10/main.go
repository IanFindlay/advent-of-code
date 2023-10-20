package main

import (
	"bufio"
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Cycle struct {
	strength int
	x        int
}

func main() {
	file, _ := os.Open("input.txt")
	scanner := bufio.NewScanner(file)
	instructions := []string{}
	for scanner.Scan() {
		instructions = append(instructions, scanner.Text())
	}

	x := 1
	currentCycle := 1
	cycles := map[int]Cycle{}
	for _, instruction := range instructions {
		cycles[currentCycle] = Cycle{strength: x * currentCycle, x: x}
		if instruction == "noop" {
			currentCycle++
		} else {
			incXBy, _ := strconv.Atoi(instruction[5:])
			currentCycle++
			cycles[currentCycle] = Cycle{strength: x * currentCycle, x: x}
			currentCycle++
			cycles[currentCycle] = Cycle{strength: x * currentCycle, x: x}
			x += incXBy
		}
	}

	strengthSum := 0
	for i := 20; ; i += 40 {
		if i > 220 {
			break
		}

		strengthSum += cycles[i].strength
	}

	fmt.Println("Answer One:", strengthSum)

	crt := []string{}
	row := []string{}
	for i := 1; i <= currentCycle; i++ {
		cycle := cycles[i]
		x := cycle.x
		pixel := i - (40 * len(crt)) - 1

		if pixel == x-1 || pixel == x || pixel == x+1 {
			row = append(row, "##")
		} else {
			row = append(row, "  ")
		}

		if (i % 40) == 0 {
			crt = append(crt, strings.Join(row, ""))
			row = []string{}
		}
	}

	fmt.Print("\nAnswer Two:\n\n")
	for _, row := range crt {
		fmt.Println(row)
	}
	fmt.Print("\n")
}
