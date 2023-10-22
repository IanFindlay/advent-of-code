package main

import (
	"encoding/json"
	"fmt"
	"os"
	"sort"
	"strings"
)

func inOrder(packet []any) int {
	left, leftIsSlice := packet[0].([]any)
	right, rightIsSlice := packet[1].([]any)

	// Both ints so compare
	if !leftIsSlice && !rightIsSlice {
		leftInt := int(packet[0].(float64))
		rightInt := int(packet[1].(float64))
		if leftInt < rightInt {
			return 1
		} else if rightInt < leftInt {
			return -1
		} else {
			return 0
		}
	}

	// Mismatched types so convert int to slice
	if !(leftIsSlice && rightIsSlice) {
		if !leftIsSlice {
			left = []any{packet[0]}
		} else {
			right = []any{packet[1]}
		}
	}

	leftLength := len(left)
	rightLength := len(right)
	var smallestLength int
	if leftLength <= rightLength {
		smallestLength = leftLength
	} else {
		smallestLength = rightLength
	}

	// Exhautively compare all values in smaller slice
	// If the order is still undecided after this, compare slice lengths
	for i := 0; i < smallestLength; i++ {
		inOrder := inOrder([]any{left[i], right[i]})
		if inOrder != 0 {
			return inOrder
		}
	}

	if leftLength < rightLength {
		return 1
	} else if rightLength < leftLength {
		return -1
	}

	return 0
}

func main() {
	file, _ := os.ReadFile("input.txt")
	packets := [][]any{}
	pairs := strings.Split(string(file), "\n\n")
	for _, pair := range pairs {
		var left, right any
		unparsedPackets := strings.Split(pair, "\n")
		json.Unmarshal([]byte(unparsedPackets[0]), &left)
		json.Unmarshal([]byte(unparsedPackets[1]), &right)

		packets = append(packets, []any{left, right})
	}

	inOrderIndiciesSum := 0
	for index, packet := range packets {
		if inOrder(packet) == 1 {
			inOrderIndiciesSum += index + 1
		}
	}

	fmt.Println("Answer One:", inOrderIndiciesSum)

	flatPackets := []any{}
	for _, packet := range packets {
		flatPackets = append(flatPackets, packet[0])
		flatPackets = append(flatPackets, packet[1])
	}

	var div1, div2 any
	json.Unmarshal([]byte("[[2]]"), &div1)
	json.Unmarshal([]byte("[[6]]"), &div2)
	flatPackets = append(flatPackets, div1)
	flatPackets = append(flatPackets, div2)

	sort.Slice(
		flatPackets,
		func(i, j int) bool {
			return inOrder([]any{flatPackets[i], flatPackets[j]}) == 1
		},
	)

	decoderKey := 1
	for index, packet := range flatPackets {
		packetString := fmt.Sprint(packet)
		if packetString == "[[2]]" || packetString == "[[6]]" {
			decoderKey *= index + 1
		}
	}

	fmt.Println("Answer Two:", decoderKey)
}
