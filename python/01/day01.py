#!/usr/bin/python
# Advent of Code 2018, day 1
# https://adventofcode.com/2018/day/1

import sys


def count(filename):
    numbers = open(filename, 'r')
    total = 0
    for line in numbers:
        total += int(line)
    return total


def find_repeat(filename):
    '''Finds the first repeated frequency value
       https://adventofcode.com/2018/day/1#part2
    '''
    def list_loop(mylist, total, frequency_set):
        for freq in mylist:
            total += int(freq)
            #print("New total is " + str(total))
            if total not in frequency_set:
                frequencies.add(total)
            else:
                return total, total, frequency_set
        
        # If we looped through all the numbers in the list and did not find a
        # repeat yet
        return None, total, frequency_set

    numbers = []
    with open(filename) as f:
        numbers = [line.rstrip() for line in f]
    total = 0
    repeat_total = None
    frequencies = set()

    while repeat_total is None:
        repeat_total, total, frequencies = list_loop(numbers, total, frequencies)

    return repeat_total


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day01.py part[1|2] <input_file>\n")
    else:
        if sys.argv[1] == 'part1':
            total = count(sys.argv[2])
            print("Resulting frequency is " + str(total))
        elif sys.argv[1] == 'part2':
            repeat = find_repeat(sys.argv[2])
            print("First repeating frequency is " + str(repeat))
        else:
            print("You must choose either 'part1' or 'part2' to run")
