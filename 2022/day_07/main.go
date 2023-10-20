package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"strconv"
	"strings"
)

type Dir struct {
	parentDir   *Dir
	childDirs   map[string]*Dir
	sumFileSize int
	size        int
}

func main() {
	file, err := os.Open("input.txt")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	rootDir := &Dir{
		parentDir: nil,
		childDirs: map[string]*Dir{},
	}

	scanner := bufio.NewScanner(file)
	currentDir := rootDir
	for scanner.Scan() {
		line := scanner.Text()
		if strings.HasPrefix(line, "$ cd") {
			dirName := line[5:]
			if dirName == ".." {
				currentDir = currentDir.parentDir

			} else if dirName == "/" {
				currentDir = rootDir
			} else {
				newCurrent := currentDir.childDirs[dirName]
				currentDir = newCurrent
			}

		} else if strings.HasPrefix(line, "$ ls") {
			continue

		} else if strings.HasPrefix(line, "dir") {
			dirName := line[4:]
			currentDir.childDirs[dirName] = &Dir{
				parentDir: currentDir,
				childDirs: map[string]*Dir{},
			}

		} else {
			splitLine := strings.Split(line, " ")
			size, err := strconv.Atoi(splitLine[0])
			if err != nil {
				log.Fatal(err)
			}
			currentDir.sumFileSize += size
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	dirList := []*Dir{}
	createDirList(rootDir, &dirList)

	calculateDirSizes(rootDir)
	answerOne := sumOfDirsSmallerThanOneHundredThousand(dirList)
	fmt.Println("Answer One:", answerOne)

	answerTwo := dirToDeleteSize(dirList, rootDir.size)
	fmt.Println("Answer Two:", answerTwo)
}

func createDirList(dir *Dir, dirList *[]*Dir) {
	for _, childDir := range dir.childDirs {
		createDirList(childDir, dirList)
	}

	*dirList = append(*dirList, dir)
}

func calculateDirSizes(dir *Dir) {
	totalSize := dir.sumFileSize
	for _, childDir := range dir.childDirs {
		calculateDirSizes(childDir)
		totalSize += childDir.size
	}

	dir.size = totalSize
}

func sumOfDirsSmallerThanOneHundredThousand(dirList []*Dir) int {
	sum := 0
	for _, childDir := range dirList {
		if childDir.size < 100000 {
			sum += childDir.size
		}
	}

	return sum
}

func dirToDeleteSize(dirList []*Dir, rootSize int) int {
	spaceToFree := 30000000 - (70000000 - rootSize)
	smallest := rootSize
	for _, childDir := range dirList {
		if childDir.size > spaceToFree && childDir.size < smallest {
			smallest = childDir.size
		}
	}

	return smallest
}
