package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	initialIdx int
	value      int
	prev       *Node
	next       *Node
}

type NodeMover interface {
	moveNode()
	findNewNextNode()
	cut()
	insertBefore(*Node)
}

func main() {
	file, _ := os.ReadFile("input.txt")
	numStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	numNodes := len(numStrs)

	headNode, nodes := buildNodes(numStrs, 1)
	mix(1, numNodes, nodes)
	groveCoords := calcGroveCoords(headNode, numStrs, 1)
	fmt.Println("Answer One:", groveCoords)

	decryptionKey := 811589153
	headNode, nodes = buildNodes(numStrs, decryptionKey)
	mix(10, numNodes, nodes)
	groveCoords = calcGroveCoords(headNode, numStrs, decryptionKey)
	fmt.Println("Answer Two:", groveCoords)
}

func buildNodes(numStrs []string, decryptionKey int) (*Node, map[int]*Node) {
	lenNums := len(numStrs)
	nodes := map[int]*Node{}
	headNode := &Node{}
	for idx, numStr := range numStrs {
		num, _ := strconv.Atoi(numStr)
		node := &Node{initialIdx: idx, value: (num * decryptionKey) % (lenNums - 1)}
		if idx != 0 {
			node.prev = nodes[idx-1]
			if idx < lenNums {
				nodes[idx-1].next = node
			}
		}
		if node.value == 0 {
			headNode = node
		}
		nodes[idx] = node
	}
	nodes[0].prev = nodes[lenNums-1]
	nodes[lenNums-1].next = nodes[0]

	return headNode, nodes
}

func mix(numMixes int, numNodes int, nodes map[int]*Node) {
	for numMixes > 0 {
		idx := 0
		for idx < numNodes {
			node := nodes[idx]
			node.moveNode(numNodes)
			idx++
		}
		numMixes--
	}
}

func (node *Node) moveNode(numNodes int) {
	node.cut()
	newNext := node.findNewNextNode(numNodes)
	node.insertBefore(newNext)
}

func (node *Node) cut() {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (node *Node) findNewNextNode(numNodes int) *Node {
	numMoves := node.value
	if node.value < 0 {
		numMoves = -numMoves
	}
	targetNode := node
	for numMoves > 0 {
		if node.value > 0 {
			targetNode = targetNode.next
		} else {
			targetNode = targetNode.prev
		}

		numMoves--
	}

	if node.value >= 0 {
		targetNode = targetNode.next
	}

	return targetNode
}

func (node *Node) insertBefore(newNext *Node) {
	node.next = newNext
	node.prev = newNext.prev
	node.prev.next = node
	node.next.prev = node
}

func calcGroveCoords(headNode *Node, numStrs []string, decryptionKey int) int {
	values := nodesToValueList(headNode, numStrs, decryptionKey)
	lenValues := len(values)

	positionsToCheck := [3]int{1000, 2000, 3000}
	groveCoords := 0
	for _, position := range positionsToCheck {
		groveCoords += values[position%lenValues]
	}

	return groveCoords
}

func nodesToValueList(headNode *Node, numStrs []string, decryptionKey int) []int {
	values := []int{}
	currentNode := headNode
	for {
		value, _ := strconv.Atoi(numStrs[currentNode.initialIdx])
		values = append(values, value*decryptionKey)
		currentNode = currentNode.next
		if currentNode == headNode {
			break
		}
	}

	return values
}
