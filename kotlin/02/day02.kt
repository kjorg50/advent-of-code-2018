// Advent of Code
// Day 02
// https://adventofcode.com/2018/day/2

import java.io.File

fun main(args: Array<String>) {
     part1("input_simple.txt")
    //println(countOccurences("aaa", 'a'))
}

fun part1(filename: String) {
    var twoLetterIds: Int = 0
    var threeLetterIds: Int = 0

    File(filename).forEachLine {
        val letterSet = it.toHashSet()
        var foundTwoLetter = false
        var foundThreeLetter = false

        for (item : Char in letterSet) {
            if ((countOccurences(it, item) == 2) and !foundTwoLetter) {
                twoLetterIds++
                foundTwoLetter = true
            }
            if ((countOccurences(it, item) == 3) and !foundThreeLetter) {
                threeLetterIds++
                foundThreeLetter = true
            }
        }
    }

    println("Part 1 answer is ${twoLetterIds * threeLetterIds}")
}

fun countOccurences(str: String, ch: Char) = str.toCharArray().filter { s -> s == ch}.count()