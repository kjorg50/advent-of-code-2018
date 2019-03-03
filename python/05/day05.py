#!/usr/bin/python
# Advent of Code 2018
# An example starter file for a given day

import sys


def isPolarOpposite(x, y):
    return abs(ord(x) - ord(y)) == 32

''' Recursion uses too much memory :( '''
# def poly_recurse(idx, poly):
#     # base case if length is 0 or 1
#     if len(poly) < 2:
#         return poly
#     # base case if the index is at the end
#     if idx > (len(poly) - 2):
#         return poly
#     # Check current and next index for polar opposites.
#     # If they are, then remove them and check the remaining string
#     #   from one index back.
#     if isPolarOpposite(poly[idx], poly[idx + 1]):
#         return poly_recurse(idx - 1, poly[:idx] + poly[idx + 2:])
#     else:
#         return poly_recurse(idx + 1, poly)


def react_polymer(poly):
    result = []
    for c in poly:
        if result and isPolarOpposite(c, result[-1]):
            result.pop()
        else:
            result.append(c)

    return result


def part1(filename):
    polymer = open(filename).read().strip()
    return len(react_polymer(polymer))


def part2(filename):
    polymer = open(filename).read().strip()
    letters = set(filter(lambda x: x.islower(), polymer))

    stuff = []
    for l in letters:
        newline = polymer.replace(l.lower(), '').replace(l.upper(), '')
        stuff.append(react_polymer(newline))

    return min(len(x) for x in stuff)


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
