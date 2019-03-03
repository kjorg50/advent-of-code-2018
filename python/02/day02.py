#!/usr/bin/python
# Advent of Code 2018, day 2
# https://adventofcode.com/2018/day/2

import sys

# From wikipedia
def _hamming_distance(s1, s2):
    """Return the Hamming distance between equal-length sequences"""
    if len(s1) != len(s2):
        raise ValueError("Undefined for sequences of unequal length")
    return sum(el1 != el2 for el1, el2 in zip(s1, s2))

def part1(filename):
    two_letter_ids = 0
    three_letter_ids = 0

    f = open(filename, 'r')
    for line in f:
        letter_set = set(list(line))
        found_two_letter = False
        found_three_letter = False
        for item in letter_set:
            c = line.count(item)
            if c == 2 and not found_two_letter:
                two_letter_ids += 1
                found_two_letter = True
            if c == 3 and not found_three_letter:
                three_letter_ids += 1
                found_three_letter = True

    return two_letter_ids * three_letter_ids


def part2(filename):
    codes = []
    correct_ids = ()
    # Extract all lines into array
    with open(filename) as f:
        codes = [line.rstrip() for line in f]
    for i in range(len(codes)):
        for j in range(i + 1, len(codes)):
            # Compare the Hamming distance of two strings
            if _hamming_distance(codes[i], codes[j]) == 1:
                correct_ids = (codes[i], codes[j])

    result = ""
    w1, w2 = correct_ids
    for i in range(len(w1)):
        if w1[i] == w2[i]:
            result += w1[i]

    return result


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day02.py part[1|2] <input_file>\n")
    else:
        if sys.argv[1] == 'part1':
            result1 = part1(sys.argv[2])
            print("Checksum is " + str(result1))
        elif sys.argv[1] == 'part2':
            result2 = part2(sys.argv[2])
            print("Output is " + str(result2))
        else:
            print("You must choose either 'part1' or 'part2' to run")
