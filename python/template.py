#!/usr/bin/python
# Advent of Code 2018
# An example starter file for a given day

import sys

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day0X.py part[1|2] <input_file>\n")
    else:
        if sys.argv[1] == 'part1':
            result1 = part1(sys.argv[2])
            print("Output is " + str(result1))
        elif sys.argv[1] == 'part2':
            result2 = part2(sys.argv[2])
            print("Output is " + str(result2))
        else:
            print("You must choose either 'part1' or 'part2' to run")
