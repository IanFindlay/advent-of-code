package main

import (
	"fmt"
	"os"
	"strconv"
	"strings"
)

type Node struct {
	value int
	prev  *Node
	next  *Node
}

type NodeOps interface {
	moveNode()
	findNewNextNode()
	cut()
	insertBefore(*Node)
}

func main() {
	file, _ := os.ReadFile("input.txt")
	numStrs := strings.Split(strings.TrimSpace(string(file)), "\n")
	headNode, nodes := buildNodes(numStrs)

	for idx := range numStrs {
		node := nodes[idx]
		node.moveNode()
	}

	values := nodesToValueList(headNode)
	lenValues := len(values)

	positionsToCheck := [3]int{1000, 2000, 3000}
	groveCoords := 0
	for _, position := range positionsToCheck {
		groveCoords += values[position%lenValues]
	}

	fmt.Println("Answer One:", groveCoords)
}

func buildNodes(numStrs []string) (*Node, map[int]*Node) {
	lenNums := len(numStrs)
	nodes := map[int]*Node{}
	headNode := &Node{}
	for idx, numStr := range numStrs {
		num, _ := strconv.Atoi(numStr)
		node := &Node{value: num}
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

func (node *Node) moveNode() {
	newNext := node.findNewNextNode()
	if newNext == node {
		return
	}
	node.cut()
	node.insertBefore(newNext)
}

func (node *Node) findNewNextNode() *Node {
	numMoves := node.value
	if node.value < 0 {
		numMoves = -node.value
	}
	targetNode := node
	for numMoves > 0 {
		if node.value > 0 {
			targetNode = targetNode.next
		} else {
			targetNode = targetNode.prev
		}

		// Moving through its own position doesn't count as an actual move
		if targetNode != node {
			numMoves--
		}
	}

	if node.value > 0 && targetNode != node {
		targetNode = targetNode.next
	}

	return targetNode
}

func (node *Node) cut() {
	node.prev.next = node.next
	node.next.prev = node.prev
}

func (node *Node) insertBefore(newNext *Node) {
	node.next = newNext
	node.prev = newNext.prev
	node.prev.next = node
	node.next.prev = node
}

func nodesToValueList(headNode *Node) []int {
	values := []int{}
	currentNode := headNode
	for {
		values = append(values, currentNode.value)
		currentNode = currentNode.next
		if currentNode == headNode {
			break
		}
	}

	return values
}
