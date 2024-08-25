package main

import (
	"fmt"
	"math"
	"os"
	"strings"
)

func main() {
	file, _ := os.ReadFile("input.txt")
	numbers := strings.Split(strings.TrimSpace(string(file)), "\n")
	symbolToNum := map[string]int{
		"=": -2,
		"-": -1,
		"0": 0,
		"1": 1,
		"2": 2,
	}

	decimalSum := 0
	for _, number := range numbers {
		value := 0
		exponent := 0
		for idx := len(number) - 1; idx >= 0; idx-- {
			char := string(number[idx])
			value += symbolToNum[char] * (int(math.Pow(5, float64(exponent))))
			exponent++
		}
		decimalSum += value
	}

	exponent := 0
	for {
		if decimalSum < int(math.Pow(5, float64(exponent)))*2 {
			break
		}
		exponent++
	}

	snafu := ""
	sum := 0
	for exponent >= 0 {
		expValue := int(math.Pow(5, float64(exponent)))
		potentialValues := map[string]int{
			"=": sum + (expValue * -2),
			"-": sum + (-expValue),
			"0": sum,
			"1": sum + expValue,
			"2": sum + (expValue * 2),
		}

		closestnewValue := math.MaxInt
		closestSymbol := ""
		for char, newValue := range potentialValues {
			if math.Abs(float64(decimalSum)-float64(newValue)) < math.Abs(float64(decimalSum)-float64(closestnewValue)) {
				closestnewValue = newValue
				closestSymbol = char
			}
		}
		snafu += closestSymbol
		sum = closestnewValue

		exponent--
	}

	fmt.Println("Answer One:", snafu)
}
