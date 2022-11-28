package main

import (
	"fmt"
	"os"
)

func main() {
	words := parseCommandLineArgs()
	printAnswer(words)
}

func parseCommandLineArgs() []string {
	cmdargs := os.Args[1:]
	return cmdargs
}

func isSeparator(char string) bool {
	return char == " " || char == "\n" || char == "\t"
}

func countWordsInString(line []string) int {
	count := 0
	for _, word := range line {
		if isSeparator(word) {
			continue
		}
		count++
	}
	return count
}

func printAnswer(line []string) {
	wordsNum := countWordsInString(line)
	if wordsNum > 0 {
		fmt.Printf("String Contains %d Words!", wordsNum)
	} else {
		fmt.Printf("String Is Empty!")
	}
}