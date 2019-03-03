// Advent of Code 
// Day 01
// https://adventofcode.com/2018/day/1

import java.io.File

fun part1(filename: String) {
    var total = 0
    File(filename).forEachLine {
        total += it.toInt()
    }
    println("The total for part1 is $total")
}

fun part2(filename: String) {
    val numbers = arrayListOf<Int>()
    File(filename).forEachLine {
        numbers.add(it.toInt())
    }

    val frequencies = mutableSetOf<Int>()
    var freq = 0

    while(true) {
        for (i in numbers) {
            freq += i

            if(frequencies.contains(freq)) {
                println("The first repeated frequency is ${freq}")
                return
            }

            frequencies += freq
        }
    }
}

fun main(args: Array<String>) {
    part1("input.txt")
    part2("input.txt")
}