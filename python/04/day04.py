#!/usr/bin/python
# Advent of Code 2018
# https://adventofcode.com/2018/day/4

import sys
from collections import defaultdict


# We are only concerned with the minute value in the timestamp
def parseTime(timestamp):
    day, time = timestamp.split(' ')
    minute = time.split(':')[1]
    return int(minute)


# We know the pattern of the messages, so the ID field will always
# be in the same spot
def parseID(text):
    return text.split(' ')[3][1:]


def part1(filename):
    lines = open(filename).read().split('\n')
    lines.sort()

    guardTotal = defaultdict(int)
    guardPerMinTotal = defaultdict(int)

    guard = None
    t1 = None
    t2 = None

    for line in lines:
        minute = parseTime(line[1:17])
        if 'begins shift' in line:
            guard = parseID(line)
        elif 'falls asleep' in line:
            t1 = minute
        elif 'wakes up' in line:
            t2 = minute
            guardTotal[guard] += (t2 - t1)
            for i in range(t1, t2):
                guardPerMinTotal[(guard, i)] += 1

    guardMax = max(guardTotal.keys(), key=(lambda k: guardTotal[k]))
    minuteMax = 0
    for k, v in guardPerMinTotal.keys():
        if k == guardMax:
            if guardPerMinTotal[(guardMax, v)] > guardPerMinTotal[(guardMax, minuteMax)]:
                minuteMax = v

    return int(guardMax) * minuteMax


def part2(filename):
    lines = open(filename).read().split('\n')
    lines.sort()

    guardTotal = defaultdict(int)
    guardPerMinTotal = defaultdict(int)

    guard = None
    t1 = None
    t2 = None

    for line in lines:
        minute = parseTime(line[1:17])
        if 'begins shift' in line:
            guard = parseID(line)
        elif 'falls asleep' in line:
            t1 = minute
        elif 'wakes up' in line:
            t2 = minute
            guardTotal[guard] += (t2 - t1)
            for i in range(t1, t2):
                guardPerMinTotal[(guard, i)] += 1

    maxG, maxM = max(guardPerMinTotal.keys(),
                     key=(lambda (g, m): guardPerMinTotal[(g, m)]))

    return int(maxG) * maxM

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python day04.py part[1|2] <input_file>\n")
    else:
        if sys.argv[1] == 'part1':
            result1 = part1(sys.argv[2])
            print("Output is " + str(result1))
        elif sys.argv[1] == 'part2':
            result2 = part2(sys.argv[2])
            print("Output is " + str(result2))
        else:
            print("You must choose either 'part1' or 'part2' to run")
